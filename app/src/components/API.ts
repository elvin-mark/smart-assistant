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

// Function to send Opus Blob to the backend
async function sendOpusBlobToBackend(opusBlob: Blob): Promise<void> {
    // Create a FormData object and append the Opus Blob
    const formData = new FormData();
    formData.append('opusAudio', opusBlob, 'audio.opus');

    try {
        // Use the fetch API to send the FormData to the backend
        const response = await fetch('http://localhost:5000/test', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Handle successful response from the backend
        console.log('Opus Blob sent successfully to the backend!');
    } catch (error) {
        console.error('Error sending Opus Blob to the backend:', error);
    }
}



export { fetchChatbotResponse, sendOpusBlobToBackend }
