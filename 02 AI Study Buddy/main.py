# Rule Based AI Python ChatBot

import datetime
import time

# Greeting Section

name = input("Welcome, enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    print("Good morning,", name)
elif 12 <= presentHour < 17:
    print("Good afternoon,", name)
elif 17 <= presentHour < 21:
    print("Good evening,", name)
else:
    print("Good night,", name)

print("Namaste! Welcome to Your Buddy ChatBot 🤖")
print("You can ask me basic questions. Type 'bye' to exit.\n")

# Chatbot Memory 

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I am doing great. Thanks for asking!",
    "who are you": "I am your smart rule-based AI chatbot.",

    "happy": "That’s wonderful to hear! Keep smiling 😄",
    "sad": "I’m sorry you’re feeling sad. Tough times pass 💙",

    "motivate": "Keep going. Every bug in your project makes you a better developer.",
    "function": "Functions are reusable blocks of code. Check chapter 7 📘",
    "weather": "Today the weather is cold with chances of rain ☁️",
    "career": "Choose a career that makes you happy and curious.",
    "programming language": "There is no best language. Choose the one that solves your problem."
}

# Response Function 

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()

    time.sleep(1)  # ⏳ 1 second delay

    for key in responses:
        if key in userQuestion:
            return responses[key]

    return "I am not able to tell that yet. I will learn this soon...."

# Chat Loop

while True:
    userInput = input("Please ask your question: ").lower()

    if "bye" in userInput:
        time.sleep(1)
        print("Bot Response: Goodbye! Take care 🌱")
        break

    reply = getResponseBot(userInput)
    print("Bot Response:", reply)
