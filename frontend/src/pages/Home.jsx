import { useEffect, useState } from "react";
import api from "../services/api";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

function Home() {

    const [characters, setCharacters] = useState([]);
    const [selected, setSelected] = useState(null);

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        loadCharacters();

    }, []);

    const getTime = () => {

        return new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit"
        });

    };

    const loadCharacters = async () => {

        try {

            const res = await api.get("/characters");

            setCharacters(res.data);

            if (res.data.length > 0) {

                const first = res.data[0];

                setSelected(first);

                welcomeMessage(first);

            }

        } catch (err) {

            console.log(err);

        }

    };

    const welcomeMessage = async (character) => {

        try {

            setLoading(true);

            const response = await api.post("/chat", {

                character_id: character.id,
                message: "Xin chào"

            });

            setMessages([

                {
                    role: "assistant",
                    content: response.data.reply,
                    time: getTime()
                }

            ]);

        } catch {

            setMessages([
                {
                    role: "assistant",
                    content: "Xin chào!",
                    time: getTime()
                }
            ]);

        }

        setLoading(false);

    };

    const sendMessage = async (message) => {

        if (!selected) return;

        const userMessage = {

            role: "user",
            content: message,
            time: getTime()

        };

        setMessages(old => [...old, userMessage]);

        setLoading(true);

        try {

            const response = await api.post("/chat", {

                character_id: selected.id,
                message: message

            });

            const aiMessage = {

                role: "assistant",
                content: response.data.reply,
                time: getTime()

            };

            setMessages(old => [...old, aiMessage]);

        }

        catch {

            setMessages(old => [

                ...old,

                {
                    role: "assistant",
                    content: "Xin lỗi, hiện tại tôi chưa thể trả lời.",
                    time: getTime()
                }

            ]);

        }

        setLoading(false);

    };

    const changeCharacter = async (character) => {

        setSelected(character);

        setMessages([]);

        await welcomeMessage(character);

    };

    return (

        <div className="container">

            <Sidebar

                characters={characters}

                selected={selected}

                onSelect={changeCharacter}

            />

            <div className="content">

                {

                    selected &&

                    <div className="header">

                        <div className="profile">

                            <img

                                className="avatar"

                                src={`http://127.0.0.1:8000/images/${selected.avatar}`}

                                alt={selected.name}

                            />

                            <div className="profile-info">

                                <h1>{selected.name}</h1>

                                <h3>{selected.occupation}</h3>

                                <p>{selected.description}</p>

                            </div>

                        </div>

                    </div>

                }

                <div className="chat-area">

                    <ChatWindow

                        messages={messages}

                        loading={loading}

                    />

                </div>

                <div className="input-area">

                    <ChatInput

                        onSend={sendMessage}

                        loading={loading}

                    />

                </div>

            </div>

        </div>

    );

}

export default Home;