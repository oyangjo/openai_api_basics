import openai

'''
Inspired by: https://www.haihai.ai/chatgpt-api/
Changed by:
    - Refactor code to have object oriented functions
    - Add creativity portion to change temperature
    - Fix bug for input quitting string
'''

openai.api_key = 'sk-yourapikey'

def get_chatbot_type():
    return input("What type of chatbot would you like to develop? ")

def get_temperature():
    while True:
        try:
            # Get user input for temperature and try converting it to an integer
            temperature = int(input("How creative do you want it to be 1-10? (Default is 5): "))
            if 1 <= temperature <= 10:
                return temperature
        except ValueError:
            pass

def main():
    # Initialize chat_history with system message
    chat_history = [{"role": "system", "content": get_chatbot_type()}]
    # Get temperature value and normalize it
    temperature = get_temperature() / 5

    print("Your chatbot is now ready! Type \'q!\' to end conversation.")
    while True:
        message = input()
        if message == 'q!':
            break
        
        # Add user message to chat_history
        chat_history.append({"role": "user", "content": message})
        # Generate chatbot response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", temperature=temperature, messages=chat_history
        )

        # Extract and display reply
        reply = response["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")

if __name__ == "__main__":
    main()