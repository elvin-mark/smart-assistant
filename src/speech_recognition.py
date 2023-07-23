from transformers import WhisperProcessor, WhisperForConditionalGeneration
import numpy as np

class SpeechRecognition:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")
    
    def transcript(self,  raw_data_buffer: np.ndarray, sampling_rate: int = 16000):
        raw_data = raw_data_buffer / pow(2, 15)
        input_features =  self.processor(raw_data, sampling_rate=sampling_rate, return_tensors="pt").input_features 
        predicted_ids = self.model.generate(input_features)
        transcription =  self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        return transcription