function MessageBubble({ sender, content }) {

    return (
        <div className={`message ${sender}`}>

            <div className="message-bubble">
                {content}
            </div>

        </div>
    );
}

export default MessageBubble;