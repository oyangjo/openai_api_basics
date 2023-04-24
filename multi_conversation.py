import openai

'''
Inspired by: https://www.haihai.ai/chatgpt-api/
'''

openai.api_key = 'sk-yourapikey'

messages = []
chatbotType = input("What type of chatbot would you like to develop? ")
messages.append({"role": "system", "content": chatbotType})

print("Your chatbot is now ready! Type \'q!\' to end conversation.")
while input != "q!": 
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
