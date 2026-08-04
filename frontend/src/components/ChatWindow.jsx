import {
    useEffect,
    useRef
} from "react";

import Message from "./Message";

function ChatWindow({
    messages = [],
    loading,
    character
}) {
    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages, loading]);

    return (
        <div className="chat-window">

            {messages.length === 0 && (
                <div className="welcome">

                    <div className="welcome-icon">
                        ✦
                    </div>

                    <h1>
                        Echoes of War
                    </h1>

                    <p>
                        Trò chuyện cùng những nhân vật
                        lịch sử và khám phá những câu
                        chuyện từ quá khứ.
                    </p>

                    {character && (
                        <div className="welcome-character">
                            Bạn đang trò chuyện cùng{" "}
                            <strong>
                                {character.name}
                            </strong>
                        </div>
                    )}

                </div>
            )}

            {messages.map(
                (message, index) => (
                    <Message
                        key={
                            message.id ||
                            `${index}-${message.content}`
                        }
                        message={message}
                    />
                )
            )}

            {loading && (
                <div className="message-row assistant">

                    <div className="message-avatar">
                        AI
                    </div>

                    <div className="typing-bubble">

                        <span></span>
                        <span></span>
                        <span></span>

                    </div>

                </div>
            )}

            <div ref={bottomRef}></div>

        </div>
    );
}

export default ChatWindow;