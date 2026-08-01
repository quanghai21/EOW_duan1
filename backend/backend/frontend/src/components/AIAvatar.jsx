import React, { useState } from 'react';
import AIAvatar from './AIAvatar';

function ChatBox() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    const sendMessage = async (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = { content: input, is_user: true };
        setMessages((prev) => [...prev, userMessage]);
        const currentInput = input;
        setInput('');
        setLoading(true);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    character_id: 1,
                    message: currentInput
                }),
            });

            const data = await response.json();

            const aiMessage = {
                content: data.reply || data.error || "Lỗi phản hồi",
                is_user: false
            };
            setMessages((prev) => [...prev, aiMessage]);
        } catch (error) {
            console.error('Lỗi kết nối API:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-screen max-w-2xl mx-auto p-4 bg-white shadow-lg rounded-lg">
            <div className="flex-1 overflow-y-auto p-4 space-y-4 border-b">
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        className={`flex items-start space-x-3 ${msg.is_user ? 'justify-end' : 'justify-start'}`}
                    >
                        {!msg.is_user && <AIAvatar />}
                        <div className={`p-3 rounded-lg max-w-md ${msg.is_user ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-800'}`}>
                            <p>{msg.content}</p>
                        </div>
                    </div>
                ))}
                {loading && <p className="text-gray-400 italic text-sm">AI đang trả lời...</p>}
            </div>

            <form onSubmit={sendMessage} className="flex mt-4 gap-2">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Nhập tin nhắn của bạn..."
                    className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                />
                <button
                    type="submit"
                    className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
                >
                    Gửi
                </button>
            </form>
        </div>
    );
}

export default ChatBox;