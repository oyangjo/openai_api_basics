import gradio as gr
import openai

'''
Inspired by Harrison Kinsley: https://twitter.com/Sentdex?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor
'''

openai.api_key = 'sk-yourapikey'

class ChatBot:
    def __init__(self):
        self.chat_history = []

    def predict(self, temperature, content):
        self.chat_history.append({"role": "user", "content": f"{content}"})

        reply = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature/5,
        messages=self.chat_history
        )

        self.chat_history.append({"role": "assistant", "content": reply.choices[0].message.content}) 
        
        response = [(self.chat_history[i]["content"], self.chat_history[i+1]["content"]) for i in range(2, len(self.chat_history)-1, 2)]  # convert to tuples of list
        return response

    def clear_history(self):
        self.chat_history = [x for x in self.chat_history[:2]]

    def main(self):
        bot_type = "You are a joke bot. I will specify the subject matter in my messages, and you will reply with a joke that includes the subjects I mention in my messages. Reply only with jokes to further input. If you understand, say OK."
        self.chat_history = [
            {"role": "system", "content": bot_type}, {"role": "assistant", "content": "OK"}
            ]

        with gr.Blocks() as demo: 
            slider = gr.Slider(minimum=1, maximum=10, step=1, default=5, label="Creativity")
            chatbot = gr.Chatbot() 
            clear = gr.Button("Clear")

            with gr.Row(): 
                txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

            txt.submit(self.predict, [slider, txt], chatbot) 
            clear.click(self.clear_history, None, chatbot, queue=False)
                
        demo.launch()       

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.main()
