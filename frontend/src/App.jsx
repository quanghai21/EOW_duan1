import { useEffect, useState } from "react";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import {
    getCharacters,
    sendChat,
    getConversations,
    getHistory,
    deleteConversation
} from "./services/api";

import "./styles/app.css";

function App() {
    const [characters, setCharacters] = useState([]);
    const [selectedCharacter, setSelectedCharacter] = useState(null);

    const [conversations, setConversations] = useState([]);
    const [conversationId, setConversationId] = useState(null);

    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        initializeApp();
    }, []);

    const initializeApp = async () => {
        await loadCharacters();
        await loadConversations();
    };

    const loadCharacters = async () => {
        try {
            const data = await getCharacters();

            const list = Array.isArray(data)
                ? data
                : data.characters || [];

            setCharacters(list);

            if (list.length > 0) {
                setSelectedCharacter(list[0]);
            }
        } catch (error) {
            console.error("CHARACTER ERROR:", error);
        }
    };

    const loadConversations = async () => {
        try {
            const data = await getConversations();

            const list = Array.isArray(data)
                ? data
                : data.conversations || [];

            setConversations(list);
        } catch (error) {
            console.error(
                "CONVERSATION ERROR:",
                error
            );
        }
    };

    const handleSelectCharacter = (character) => {
        setSelectedCharacter(character);
        setConversationId(null);
        setMessages([]);
    };

    const handleNewConversation = () => {
        setConversationId(null);
        setMessages([]);
    };

    const handleSelectConversation = async (
        conversation
    ) => {
        if (!conversation) {
            return;
        }

        try {
            setLoading(true);

            setConversationId(conversation.id);

            const character = characters.find(
                (item) =>
                    item.id ===
                    conversation.character_id
            );

            if (character) {
                setSelectedCharacter(character);
            }

            const data = await getHistory(
                conversation.id
            );

            const history = Array.isArray(data)
                ? data
                : data.messages || [];

            const formatted = history.map(
                (item) => {
                    const role =
                        item.sender ||
                        item.role ||
                        item.type ||
                        "";

                    return {
                        id: item.id,
                        sender:
                            role === "user"
                                ? "user"
                                : "assistant",
                        content:
                            item.content ||
                            item.message ||
                            item.text ||
                            ""
                    };
                }
            );

            setMessages(formatted);
        } catch (error) {
            console.error(
                "HISTORY ERROR:",
                error
            );

            setMessages([]);
        } finally {
            setLoading(false);
        }
    };

    const handleDeleteConversation = async (
        id
    ) => {
        const confirmed = window.confirm(
            "Bạn có chắc muốn xóa cuộc trò chuyện này?"
        );

        if (!confirmed) {
            return;
        }

        try {
            await deleteConversation(id);

            setConversations((prev) =>
                prev.filter(
                    (item) => item.id !== id
                )
            );

            if (conversationId === id) {
                setConversationId(null);
                setMessages([]);
            }
        } catch (error) {
            console.error(
                "DELETE ERROR:",
                error
            );

            alert(
                "Không thể xóa cuộc trò chuyện."
            );
        }
    };

    const sendMessage = async (message) => {
        const text = message?.trim();

        if (
            !text ||
            loading ||
            !selectedCharacter
        ) {
            return;
        }

        setMessages((prev) => [
            ...prev,
            {
                sender: "user",
                content: text
            }
        ]);

        setLoading(true);

        try {
            const data = await sendChat(
                selectedCharacter.id,
                text,
                conversationId
            );

            if (
                data.conversation_id !==
                undefined
            ) {
                setConversationId(
                    data.conversation_id
                );
            }

            setMessages((prev) => [
                ...prev,
                {
                    sender: "assistant",
                    content:
                        data.reply ||
                        "Xin lỗi, tôi chưa thể trả lời."
                }
            ]);

            await loadConversations();
        } catch (error) {
            console.error(
                "CHAT ERROR:",
                error
            );

            setMessages((prev) => [
                ...prev,
                {
                    sender: "assistant",
                    content:
                        "Xin lỗi, hiện tại tôi chưa thể trả lời."
                }
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app">

            <Sidebar
                characters={characters}
                selectedCharacter={selectedCharacter}
                onSelectCharacter={
                    handleSelectCharacter
                }
                conversations={conversations}
                activeConversationId={
                    conversationId
                }
                onSelectConversation={
                    handleSelectConversation
                }
                onNewConversation={
                    handleNewConversation
                }
                onDeleteConversation={
                    handleDeleteConversation
                }
            />

            <main className="main-content">

                <Header
                    character={selectedCharacter}
                />

                <ChatWindow
                    messages={messages}
                    loading={loading}
                    character={selectedCharacter}
                />

                <ChatInput
                    onSend={sendMessage}
                    loading={loading}
                />

            </main>

        </div>
    );
}

export default App;