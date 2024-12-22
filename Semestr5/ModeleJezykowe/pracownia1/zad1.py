from transformers import pipeline
import asyncio

print("Ładowanie modelu...")
chatbot = pipeline("text-generation", model="eryk-mazus/polka-1.1b")
print("Załadowano model!")

async def generate_response(prompt):
    response = chatbot(
        prompt, 
        max_new_tokens=50, 
        min_length=20, 
        num_return_sequences=1, 
        do_sample=True, 
        top_k=50, 
        top_p=0.95, 
        return_full_text=False
    )
    await asyncio.sleep(1)
    return response[0]['generated_text']

async def generate_responses(prompt, num_responses=3):
    responses = chatbot(
        prompt,
        max_new_tokens=50,
        min_length=20,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        return_full_text=False
    )
    await asyncio.sleep(1)
    return [response['generated_text'] for response in responses]

def select_best_response(responses):
    # criterium: answer with highest average word length
    best_response = ""
    highest_avg_word_length = 0
    for response in responses:
        words = response.split()
        if words:
            avg_word_length = sum(len(word) for word in words) / len(words)
            if avg_word_length > highest_avg_word_length:
                highest_avg_word_length = avg_word_length
                best_response = response
    return best_response

def build_prompt_for_history(dialog_history, user_input, max_history=3):
    return dialog_history[-3] + "\n" + dialog_history[-2] + "\n" + dialog_history[-1] + "\n"

async def chat_no_history(start_message="Cześć!", bot_name="Czatbot Polka", user_name="Ty"):
    print(f"{bot_name}: {start_message}")
    
    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() in ['koniec', 'exit', 'quit']:
            print(f"{bot_name}: Do zobaczenia!")
            break
        
        response = await generate_response(user_input)
        print(f"{bot_name}: {response}")

async def chat_with_history(start_message="Cześć!", bot_name="Chatbot Polka", user_name="Ty"):
    print(f"{bot_name}: {start_message}")
    dialog_history = [start_message]
    first_prompt = True

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() in ['koniec', 'exit', 'quit']:
            print(f"{bot_name}: Do zobaczenia!")
            break

        dialog_history.append(user_input)
        response = ""
        if(first_prompt):
            response = await generate_response(user_input)
            first_prompt = False
        else:
            response = await generate_response(build_prompt_for_history(dialog_history, user_input))
        dialog_history.append(response)
        print(f"{bot_name}: {response}")

async def chat_with_best_response(start_message="Cześć!", bot_name="Chatbot Polka", user_name="Ty"):
    print(f"{bot_name}: {start_message}")
    dialog_history = [start_message]
    first_prompt = True

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() in ['koniec', 'exit', 'quit']:
            print(f"{bot_name}: Do zobaczenia!")
            break

        dialog_history.append(user_input)
        if first_prompt:
            responses = await generate_responses(user_input)
            first_prompt = False
        else:
            responses = await generate_responses(build_prompt_for_history(dialog_history, user_input))

        best_response = select_best_response(responses)
        dialog_history.append(best_response)
        print(f"{bot_name}: {best_response}")
        

if __name__ == "__main__":
    asyncio.run(chat_with_best_response())