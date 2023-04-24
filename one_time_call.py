import openai

openai.api_key = 'sk-yourapikey'

content = 'Knock knock joke'
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301", 
    messages=[{"role": "user", "content": content}],
    temperature=1
)
    
print(response.choices[0].message.content)