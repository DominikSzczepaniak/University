from transformers import pipeline
import torch

# Initialize the pipeline
gpt2 = pipeline('text-generation', model='eryk-mazus/polka-1.1b')
tokenizer = gpt2.tokenizer
model = gpt2.model

# Define the generate_response function
def generate_response(prompt, max_length=50, temperature=0.7):
    """
    Generates a response based on the input prompt.

    Args:
    - prompt (str): The text prompt to generate a response for.
    - max_length (int): The maximum number of tokens for the response. Default is 50.
    - temperature (float): Sampling temperature. Default is 0.7.

    Returns:
    - str: Generated response.
    """
    # Generate text using the pipeline
    response = gpt2(
        prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        truncation=True
    )
    
    # Extract and return the generated text
    return response[0]['generated_text']

# Example usage
prompt = "Once upon a time"
print(generate_response(prompt))