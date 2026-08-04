function Message({ message }) {
    const isUser =
        message.sender === "user";

    return (
        <div
            className={
                isUser
                    ? "message-row user"
                    : "message-row assistant"
            }
        >

            {!isUser && (
                <div className="message-avatar">
                    AI
                </div>
            )}

            <div
                className={
                    isUser
                        ? "message-bubble user-bubble"
                        : "message-bubble assistant-bubble"
                }
            >
                {message.content}
            </div>

        </div>
    );
}

export default Message;