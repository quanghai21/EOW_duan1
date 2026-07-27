import { useRef, useState } from "react";

function ChatInput({ onSend }) {

    const [text, setText] = useState("");

    const textareaRef = useRef(null);

    const resizeTextarea = () => {

        textareaRef.current.style.height = "auto";

        textareaRef.current.style.height =
            textareaRef.current.scrollHeight + "px";

    };

    const handleChange = (e) => {

        setText(e.target.value);

        resizeTextarea();

    };

    const send = () => {

        if (text.trim() === "") return;

        onSend(text.trim());

        setText("");

        textareaRef.current.style.height = "48px";

    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter" && !e.shiftKey) {

            e.preventDefault();

            send();

        }

    };

    return (

        <div className="chat-input">

            <textarea

                ref={textareaRef}

                rows={1}

                value={text}

                placeholder="Nhập câu hỏi..."

                onChange={handleChange}

                onKeyDown={handleKeyDown}

            />

            <button onClick={send}>

                Gửi

            </button>

        </div>

    );

}

export default ChatInput;