import { useEffect, useRef } from "react";
import Message from "./Message";

function ChatWindow({ messages, loading }) {
    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, loading]);

    return (
        <div className="chat-window">
            {messages.map((message, index) => (
                <Message
                    key={index}
                    message={message}
                    avatar="http://127.0.0.1:8000/images/dang_thuy_tram.jpg"
                />
            ))}

            {loading && (
                <div className="ai-message">
                    <strong>Đặng Thùy Trâm</strong>

                    <div className="loading">
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