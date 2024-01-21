interface ChatBotResponse {
    result: string
}

async function fetchChatbotResponse(query: string): Promise<ChatBotResponse> {
    try {
        const response = await fetch(`http://localhost:5000/chatbot/response?query=${query}`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data as ChatBotResponse;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export { fetchChatbotResponse }
