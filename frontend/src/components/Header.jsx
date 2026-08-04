function Header({ character }) {
    if (!character) {
        return (
            <header className="chat-header">

                <div className="header-title">
                    Echoes of War
                </div>

            </header>
        );
    }

    return (
        <header className="chat-header">

            <div className="header-character">

                <img
                    src={
                        character.avatar
                            ? `http://127.0.0.1:8000/static/avatars/${character.avatar}`
                            : "/default-avatar.png"
                    }
                    alt={character.name}
                    className="header-avatar"
                    onError={(event) => {
                        event.currentTarget.src =
                            "/default-avatar.png";
                    }}
                />

                <div>

                    <div className="header-name">
                        {character.name}
                    </div>

                    <div className="header-status">
                        <span className="status-dot"></span>
                        Đang sẵn sàng trò chuyện
                    </div>

                </div>

            </div>

        </header>
    );
}

export default Header;