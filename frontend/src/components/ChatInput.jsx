import {
    useState
} from "react";

function ChatInput({
    onSend,
    loading
}) {
    const [message, setMessage] =
        useState("");

    const handleSubmit = (event) => {
        event.preventDefault();

        if (
            !message.trim() ||
            loading
        ) {
            return;
        }

        onSend(message);

        setMessage("");
    };

    const handleKeyDown = (event) => {
        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {
            event.preventDefault();

            handleSubmit(event);
        }
    };

    return (
        <div className="chat-input-container">

            <form
                className="chat-input-form"
                onSubmit={handleSubmit}
            >

                <textarea
                    value={message}
                    onChange={(event) =>
                        setMessage(
                            event.target.value
                        )
                    }
                    onKeyDown={handleKeyDown}
                    placeholder={
                        "Nhập tin nhắn..."
                    }
                    disabled={loading}
                    rows={1}
                />

                <button
                    type="submit"
                    disabled={
                        loading ||
                        !message.trim()
                    }
                    className="send-button"
                >
                    {loading
                        ? "..."
                        : "➤"}
                </button>

            </form>

            <div className="input-hint">
                Enter để gửi · Shift + Enter để xuống dòng
            </div>

        </div>
    );
}

export default ChatInput;