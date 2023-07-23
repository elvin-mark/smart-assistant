from transformers import AutoProcessor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import numpy as np
from datasets import load_dataset
import torch


class Text2Speech:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained("microsoft/speecht5_tts" )

        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
        self.embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

    def generate(self,txt: str) -> torch.Tensor:
        inputs_ids = self.processor(text=txt, return_tensors="pt").input_ids
        speaker_embeddings = torch.tensor(self.embeddings_dataset[7306]["xvector"]).unsqueeze(0)
        return self.model.generate_speech(inputs_ids, speaker_embeddings, vocoder=self.vocoder)