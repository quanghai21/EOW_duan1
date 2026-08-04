function Sidebar({
    characters = [],
    selectedCharacter,
    onSelectCharacter,
    conversations = [],
    activeConversationId,
    onSelectConversation,
    onNewConversation,
    onDeleteConversation
}) {
    const characterList = Array.isArray(characters)
        ? characters
        : [];

    const conversationList = Array.isArray(
        conversations
    )
        ? conversations
        : [];

    return (
        <aside className="sidebar">

            <div className="sidebar-top">

                <div className="logo">
                    Echoes of War
                </div>

                <div className="logo-subtitle">
                    Những ký ức còn vang vọng
                </div>

                <button
                    className="new-chat-button"
                    onClick={onNewConversation}
                >
                    <span>＋</span>
                    Cuộc trò chuyện mới
                </button>

            </div>

            <div className="sidebar-section">

                <div className="section-title">
                    Nhân vật lịch sử
                </div>

                <div className="character-list">

                    {characterList.map(
                        (character) => (
                            <button
                                key={character.id}
                                className={
                                    selectedCharacter?.id ===
                                    character.id
                                        ? "character-item active"
                                        : "character-item"
                                }
                                onClick={() =>
                                    onSelectCharacter(
                                        character
                                    )
                                }
                            >

                                <img
                                    src={
                                        character.avatar
                                            ? `http://127.0.0.1:8000/static/avatars/${character.avatar}`
                                            : "/default-avatar.png"
                                    }
                                    alt={
                                        character.name
                                    }
                                    className="sidebar-avatar"
                                    onError={(event) => {
                                        event.currentTarget.src =
                                            "/default-avatar.png";
                                    }}
                                />

                                <div className="character-info">

                                    <div className="character-name">
                                        {
                                            character.name
                                        }
                                    </div>

                                    <div className="character-occupation">
                                        {
                                            character.occupation ||
                                            "Nhân vật lịch sử"
                                        }
                                    </div>

                                </div>

                            </button>
                        )
                    )}

                </div>

            </div>

            <div className="sidebar-section conversation-section">

                <div className="section-title">
                    Lịch sử trò chuyện
                </div>

                <div className="conversation-list">

                    {conversationList.length === 0 && (
                        <div className="empty-conversations">
                            Chưa có cuộc trò chuyện
                        </div>
                    )}

                    {conversationList.map(
                        (conversation) => {

                            const active =
                                conversation.id ===
                                activeConversationId;

                            const character =
                                characterList.find(
                                    (item) =>
                                        item.id ===
                                        conversation.character_id
                                );

                            return (
                                <div
                                    key={
                                        conversation.id
                                    }
                                    className={
                                        active
                                            ? "conversation-item active"
                                            : "conversation-item"
                                    }
                                >

                                    <button
                                        className="conversation-main"
                                        onClick={() =>
                                            onSelectConversation(
                                                conversation
                                            )
                                        }
                                    >

                                        <div className="conversation-icon">
                                            💬
                                        </div>

                                        <div className="conversation-info">

                                            <div className="conversation-title">
                                                {character
                                                    ?.name ||
                                                    `Cuộc trò chuyện ${conversation.id}`}
                                            </div>

                                            <div className="conversation-date">
                                                #{conversation.id}
                                            </div>

                                        </div>

                                    </button>

                                    <button
                                        className="delete-button"
                                        title="Xóa cuộc trò chuyện"
                                        onClick={() =>
                                            onDeleteConversation(
                                                conversation.id
                                            )
                                        }
                                    >
                                        ×
                                    </button>

                                </div>
                            );
                        }
                    )}

                </div>

            </div>

        </aside>
    );
}

export default Sidebar;