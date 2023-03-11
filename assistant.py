import numpy as np
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import AutoProcessor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import re


class SmartAssistant:
    def __init__(self, speech_recog_model: str = "openai/whisper-tiny.en", text2text_model: str = "google/flan-t5-small", speech_gen_mode: str = "microsoft/speecht5_tts", vocoder: str = "microsoft/speecht5_hifigan", embeddings_ds: str = "Matthijs/cmu-arctic-xvectors"):
        self.processor_speech_recog = AutoProcessor.from_pretrained(
            speech_recog_model)
        self.model_speech_recog = AutoModelForSpeechSeq2Seq.from_pretrained(
            speech_recog_model)

        self.tokenizer_text2text = AutoTokenizer.from_pretrained(
            text2text_model)

        self.model_text2text = AutoModelForSeq2SeqLM.from_pretrained(
            text2text_model)

        self.processor_text2speech = AutoProcessor.from_pretrained(speech_gen_mode
                                                                   )

        self.model_text2speech = SpeechT5ForTextToSpeech.from_pretrained(
            speech_gen_mode)
        self.vocoder = SpeechT5HifiGan.from_pretrained(
            vocoder)

        self.embeddings_dataset = load_dataset(
            embeddings_ds, split="validation")

    def speech_recognition(self, raw_data_buffer: np.ndarray, sampling_rate: int = 16000):
        raw_data = raw_data_buffer / pow(2, 15)
        input_features = self.processor_speech_recog(
            raw_data, sampling_rate=sampling_rate, return_tensors="pt").input_features
        predicted_ids = self.model_speech_recog.generate(input_features)
        transcription = self.processor_speech_recog.batch_decode(
            predicted_ids, skip_special_tokens=False)
        return re.sub('\<(.*?)\>', '', transcription[0])

    def chatbot_response(self, query: str) -> str:
        input_ids = self.tokenizer_text2text(
            query, return_tensors="pt").input_ids
        outputs = self.model_text2text.generate(input_ids)
        return self.tokenizer_text2text.decode(outputs[0], skip_special_tokens=True)

    def speech_generation(self, query: str) -> torch.Tensor:
        inputs_ids = self.processor_text2speech(
            text=query, return_tensors="pt").input_ids
        speaker_embeddings = torch.tensor(
            self.embeddings_dataset[7306]["xvector"]).unsqueeze(0)
        return self.model_text2speech.generate_speech(
            inputs_ids, speaker_embeddings, vocoder=self.vocoder)
