from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Chatbot:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    def get_response(self,query:str):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)