from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Chatbot:
    def __init__(self):
        # self.model_name = "google/flan-t5-small"
        self.model_name = "facebook/blenderbot-400M-distill"
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def get_response(self,query:str):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)