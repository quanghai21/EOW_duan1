import { useEffect, useState } from "react";
import api from "../services/api";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

function Home() {

    const [characters, setCharacters] = useState([]);
    const [selected, setSelected] = useState(null);
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        loadCharacters();
    }, []);

    const currentTime = () => {

        return new Date().toLocaleTimeString([], {

            hour: "2-digit",
            minute: "2-digit"

        });

    };

    const loadCharacters = async () => {

        try {

            const res = await api.get("/characters");

            setCharacters(res.data);

            if (res.data.length > 0) {

                changeCharacter(res.data[0]);

            }

        } catch (err) {

            console.log(err);

        }

    };

    const changeCharacter = async (character) => {

        setSelected(character);

        setMessages([]);

        setLoading(true);

        try {

            const response = await api.post("/chat", {

                character_id: character.id,
                message: "Xin chào"

            });

            setMessages([

                {

                    role: "assistant",

                    content: response.data.reply,

                    time: currentTime()

                }

            ]);

        } catch (err) {

            console.log(err);

        }

        setLoading(false);

    };

    const sendMessage = async (text) => {

        if (!selected) return;

        const user = {

            role: "user",

            content: text,

            time: currentTime()

        };

        setMessages(old => [...old, user]);

        setLoading(true);

        try {

            const response = await api.post("/chat", {

                character_id: selected.id,

                message: text

            });

            const ai = {

                role: "assistant",

                content: response.data.reply,

                time: currentTime()

            };

            setMessages(old => [...old, ai]);

        }

        catch (err) {

            console.log(err);

        }

        setLoading(false);

    };

    return (

        <div className="container">

            <Sidebar

                characters={characters}

                selected={selected}

                onSelect={changeCharacter}

            />

            <div className="content">

                {

                    selected && (

                        <div className="header">

                            <img

                                src={`http://127.0.0.1:8000/images/${selected.avatar}`}

                                className="avatar"

                                alt={selected.name}

                            />

                            <div>

                                <h1>{selected.name}</h1>

                                <h3>{selected.occupation}</h3>

                                <p>{selected.description}</p>

                            </div>

                        </div>

                    )

                }

                <ChatWindow

                    messages={messages}

                    loading={loading}

                />

                <ChatInput

                    onSend={sendMessage}

                />

            </div>

        </div>

    );

}

export default Home;