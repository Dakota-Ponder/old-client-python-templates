# first need to install pip install transformers torch
# chatbot.py
# program uses GPT-2 to generate responses to user input.
# when chatting, it tokenizes user input, feeds it to the model,
# and generates a response.

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class ChatBot:
    def __init__(self):
        # Initialize the tokenizer and model. We're using the "gpt2-medium" model for this example.
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

        # Ensure the model is in evaluation mode
        self.model.eval()

    def generate_response(self, input_text):
        """Generate a response to the input text."""
        # Tokenize the input text
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')

        # Generate a response from the model
        output = self.model.generate(
            input_ids, max_length=150, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)

        # Decode the response
        response = self.tokenizer.decode(
            output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

    def chat(self):
        """Interactive chat with the bot."""
        print("ChatBot (type 'quit' to exit)")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            response = self.generate_response(user_input)
            print(f"Bot: {response}")


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
