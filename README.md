# smart-assistant

Simple Smart Assistant that uses simple SOTA light Deep Learning models.

# Backbone

These are the services that are the "brain" of the smart assistant.

## [Chatbot](https://github.com/elvin-mark/smart-assistant/tree/main/chatbot)

This chatbot will act as the "reasoning" part of our Smart Assistant. It uses a light LLM model, in this case Gemma3. It will receive a text prompt and reply with a text response after "thinking" about it.

## [Embeddings](https://github.com/elvin-mark/smart-assistant/tree/main/embeddings)

The embedding service will act as a "knowledge manager". It will allows the Smart Assistant to encode "knowledge" in a latent space so it will be easier to find later. This will be used mainly by the RAG. For this project, we are using a very light and good enough embedding model, the all-MiniLM-L6-v2 model.

## [Speech Recognition](https://github.com/elvin-mark/smart-assistant/tree/main/speech-recognition)

Since we want to interact with voice with our Smart Assistant (not just text), we need to be able to automatically recognize the speech of the user. For this purpose, we are using the Whisper model.

## [Text-to-Speech](https://github.com/elvin-mark/smart-assistant/tree/main/text-to-speech)

Also we would like to hear the response from the assistant through audio (not just text on a screen). For this, we are using a very popular and light weight text-to-speech model: KokoroTTS.
