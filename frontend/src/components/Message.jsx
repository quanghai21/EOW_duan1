function Message({ message, avatar }) {

    const isUser = message.role === "user";

    return (

        <div className={isUser ? "message user" : "message ai"}>

            {

                !isUser && (

                    <img
                        className="message-avatar"
                        src={avatar}
                        alt="AI"
                    />

                )

            }

            <div className="message-content">

                <div className="bubble">

                    {message.content}

                </div>

                <div className="message-time">

                    {message.time}

                </div>

            </div>

            {

                isUser && (

                    <div className="user-avatar">

                        Bạn

                    </div>

                )

            }

        </div>

    );

}

export default Message;