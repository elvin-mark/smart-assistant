import torch
from transformers import pipeline
from transformers import VitsModel, AutoTokenizer
from transformers import WhisperProcessor, WhisperForConditionalGeneration


class SmartAssistant:
    def __init__(self):
        # Text Generation 
        # Model used: TinyLlama
        # Ref: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
        self.text_generation_pipeline = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")
        
        # Text To Speech
        self.text_to_speech_model = VitsModel.from_pretrained("facebook/mms-tts-eng")
        self.text_to_speech_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

        # Speech To Text
        # Model used: Whisper (tiny model)
        # Ref: https://huggingface.co/openai/whisper-tiny.en
        self.speech_to_text_processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
        self.speech_to_text_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")
    
    def chatbot_response(self, user_prompt, max_new_tokens=256):
        messages = [
            {
                "role": "system",
                "content": "You are a friendly chatbot who always responds very concisely",
            },
            {"role": "user", "content": user_prompt},
        ]
        prompt = self.text_generation_pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.text_generation_pipeline(prompt, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
        return outputs[0]["generated_text"]
    
    def generate_speech(self, text):
        inputs = self.text_to_speech_tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            output = self.text_to_speech_model(**inputs).waveform
        return output

    def transcript(self, raw_data, sampling_rate=16000):
        input_features = self.speech_to_text_processor(raw_data, sampling_rate=sampling_rate, return_tensors="pt").input_features 
        predicted_ids = self.speech_to_text_model.generate(input_features)
        transcription = self.speech_to_text_processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription

    def converse(self, user_prompt="", raw_data=None, get_audio=True):
        if user_prompt == "":
            user_prompt = self.transcript(raw_data)[0]
        response = self.chatbot_response(user_prompt)
        assistant_response = response.split("<|assistant|>")[1]
        assistant_response_audio = None
        if get_audio:
            assistant_response_audio = self.generate_speech(assistant_response)
        return assistant_response, assistant_response_audio