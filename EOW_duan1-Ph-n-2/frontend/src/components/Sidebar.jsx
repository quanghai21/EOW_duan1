function Sidebar({ characters, selected, onSelect }) {

    return (

        <div className="sidebar">

            <h2>Echoes of War</h2>

            {

                characters.map((character) => (

                    <div
                        key={character.id}
                        className={
                            selected?.id === character.id
                                ? "character active"
                                : "character"
                        }
                        onClick={() => onSelect(character)}
                    >

                        <img
                            src={`http://127.0.0.1:8000/images/${character.avatar}`}
                            className="sidebar-avatar"
                            alt={character.name}
                        />

                        <div>

                            <strong>{character.name}</strong>

                            <p>{character.occupation}</p>

                        </div>

                    </div>

                ))

            }

        </div>

    );

}

export default Sidebar;