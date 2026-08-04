const API_URL = "http://127.0.0.1:8000/api";

async function parseResponse(response) {
    const text = await response.text();

    let data = {};

    try {
        data = text ? JSON.parse(text) : {};
    } catch {
        data = {
            detail: text || "Server trả về dữ liệu không hợp lệ"
        };
    }

    if (!response.ok) {
        throw new Error(
            data.detail ||
            data.message ||
            `API Error: ${response.status}`
        );
    }

    return data;
}

export async function getCharacters() {
    const response = await fetch(
        `${API_URL}/characters`,
        {
            method: "GET",
            headers: {
                Accept: "application/json"
            }
        }
    );

    return parseResponse(response);
}

export async function sendChat(
    characterId,
    message,
    conversationId = null
) {
    const body = {
        character_id: characterId,
        message: message
    };

    if (
        conversationId !== null &&
        conversationId !== undefined
    ) {
        body.conversation_id = conversationId;
    }

    const response = await fetch(
        `${API_URL}/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json"
            },
            body: JSON.stringify(body)
        }
    );

    return parseResponse(response);
}

export async function getConversations() {
    const response = await fetch(
        `${API_URL}/conversations`,
        {
            method: "GET",
            headers: {
                Accept: "application/json"
            }
        }
    );

    return parseResponse(response);
}

export async function getConversation(
    conversationId
) {
    const response = await fetch(
        `${API_URL}/conversations/${conversationId}`,
        {
            method: "GET",
            headers: {
                Accept: "application/json"
            }
        }
    );

    return parseResponse(response);
}

export async function getHistory(
    conversationId
) {
    const response = await fetch(
        `${API_URL}/history/${conversationId}`,
        {
            method: "GET",
            headers: {
                Accept: "application/json"
            }
        }
    );

    return parseResponse(response);
}

export async function deleteConversation(
    conversationId
) {
    const response = await fetch(
        `${API_URL}/conversations/${conversationId}`,
        {
            method: "DELETE",
            headers: {
                Accept: "application/json"
            }
        }
    );

    return parseResponse(response);
}