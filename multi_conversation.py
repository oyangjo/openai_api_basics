import openai

'''
Inspired by: https://www.haihai.ai/chatgpt-api/
Tweaked by adding creativity portion to change temperature
Also, fixed bug for input quitting string
'''

openai.api_key = 'sk-yourapikey'

#initialization for params
chat_history, temperature = [], 0
chatbotType = input("What type of chatbot would you like to develop? ") 
while temperature > 10 or temperature < 1:
    temperature = int(input("How creative do you want it to be 1-10? (Default is 5): "))
chat_history.append({"role": "system", "content": chatbotType})

#begin conversation
print("Your chatbot is now ready! Type \'q!\' to end conversation.")
while True: 
    message = input()
    if message == 'q!': #break if quit
        break

    chat_history.append({"role": "user", "content": message}) 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", temperature = int(temperature)/5, messages=chat_history
        )

    reply = response["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
