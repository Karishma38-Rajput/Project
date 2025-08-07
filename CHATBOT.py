# chatbot_karishma.py
# Made by: Karishma Rajput 🌿
# A friendly chatbot using if-else based responses

import time

def bot_reply(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 👋 I'm here to chat with you."
    
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm feeling awesome! 😄"

    elif "your name" in user_input:
        return "You can call me 'KBot' — made by Karishma 💻"

    elif "who made you" in user_input:
        return "I was built with love by Karishma Rajput ❤️"

    elif "time" in user_input:
        current_time = time.strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"

    elif "thank" in user_input:
        return "You're most welcome! 😊"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! It was nice talking to you. 🌸"
    
    else:
        return "Hmm... I didn't get that. Can you say it differently?"

def start_chat():
    print("🤖 Welcome to KBot (Karishma's Chatbot)")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user_msg = input("You: ")
        reply = bot_reply(user_msg)
        print(f"KBot: {reply}\n")

        if "bye" in user_msg.lower() or "exit" in user_msg.lower():
            break

if __name__ == "__main__":
    start_chat()
