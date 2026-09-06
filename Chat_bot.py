import random
from datetime import datetime

print("====================================")
print(" WELCOME TO MY CHATBOT")
print("====================================")
print("Bot: Hello! I am a simple chatbot.")
print("Bot: You can ask me different questions.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to exit.")
print("====================================")
user=""

while True:

    # Get input from user
    user = input("You: ")

    # Convert input to lowercase
    user = user.lower()

    # Remove extra spaces
    user = user.strip()


    # --------------------------------
    # GREETING
    # --------------------------------

    if user == "hello" or user == "hi" or user == "hey":

        responses = [
            "Hello! How are you?",
            "Hi! Nice to meet you.",
            "Hey! How can I help you?"
        ]

        print("Bot:", random.choice(responses))


    # --------------------------------
    # HOW ARE YOU
    # --------------------------------

    elif "how are you" in user:

        print("Bot: I am fine! Thanks for asking.")
        print("Bot: How are you doing?")


    # --------------------------------
    # USER'S NAME
    # --------------------------------

    elif "my name is" in user:

        name = user.replace("my name is", "").strip()

        if name:
            print("Bot: Nice to meet you,", name)
        else:
            print("Bot: Nice to meet you!")


    # --------------------------------
    # BOT NAME
    # --------------------------------

    elif "your name" in user or "who are you" in user:

        print("Bot: My name is RuleBot.")
        print("Bot: I am a simple rule-based chatbot made using Python.")


    # --------------------------------
    # CREATOR
    # --------------------------------

    elif "who created you" in user or "who made you" in user:

        print("Bot: I was created using Python.")
        print("Bot: I am a rule-based chatbot project.")


    # --------------------------------
    # PYTHON
    # --------------------------------

    elif "what is python" in user or "tell me about python" in user:

        print("Bot: Python is a high-level programming language.")
        print("Bot: It is easy to learn and widely used.")
        print("Bot: Python is used in AI, web development,")
        print("Bot: data science, automation and many other fields.")


    # --------------------------------
    # PROGRAMMING
    # --------------------------------

    elif "programming" in user or "coding" in user:

        print("Bot: Programming means writing instructions")
        print("Bot: that a computer can understand and execute.")
        print("Bot: Python is a great language for beginners.")


    # --------------------------------
    # STUDY
    # --------------------------------

    elif "study" in user or "studying" in user:

        print("Bot: Here are some study tips:")
        print("Bot: 1. Create a study schedule.")
        print("Bot: 2. Study one topic at a time.")
        print("Bot: 3. Take short breaks.")
        print("Bot: 4. Practice what you learn.")
        print("Bot: 5. Revise regularly.")


    # --------------------------------
    # EXAM
    # --------------------------------

    elif "exam" in user or "exams" in user:

        print("Bot: Don't worry about your exams!")
        print("Bot: Make a timetable and study consistently.")
        print("Bot: Practice previous questions.")
        print("Bot: Get enough sleep before the exam.")


    # --------------------------------
    # COLLEGE
    # --------------------------------

    elif "college" in user:

        print("Bot: College is a great place to learn new skills.")
        print("Bot: Try to balance studies, projects and activities.")


    # --------------------------------
    # SCHOOL
    # --------------------------------

    elif "school" in user:

        print("Bot: School is an important part of learning.")
        print("Bot: Always be curious and ask questions.")


    # --------------------------------
    # JOKE
    # --------------------------------

    elif "joke" in user:

        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the computer cold? Because it left its Windows open!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "What do computers eat? Microchips!"
        ]

        print("Bot:", random.choice(jokes))


    # --------------------------------
    # HAPPY
    # --------------------------------

    elif "i am happy" in user or "i'm happy" in user:

        print("Bot: That's great!")
        print("Bot: I am happy to hear that.")


    # --------------------------------
    # SAD
    # --------------------------------

    elif "i am sad" in user or "i'm sad" in user:

        print("Bot: I am sorry to hear that.")
        print("Bot: I hope you feel better soon.")
        print("Bot: Remember, difficult days don't last forever.")


    # --------------------------------
    # THANK YOU
    # --------------------------------

    elif "thank you" in user or "thanks" in user:

        print("Bot: You're welcome!")
        print("Bot: Happy to help!")


    # --------------------------------
    # WEATHER
    # --------------------------------

    elif "weather" in user:

        print("Bot: I cannot check live weather yet.")
        print("Bot: This version of the chatbot works using predefined rules.")


    # --------------------------------
    # TIME
    # --------------------------------

    elif "time" in user:

        current_time = datetime.now().strftime("%I:%M %p")

        print("Bot: The current time is", current_time)


    # --------------------------------
    # DATE
    # --------------------------------

    elif "date" in user or "today" in user:

        current_date = datetime.now().strftime("%d-%m-%Y")

        print("Bot: Today's date is", current_date)


    # --------------------------------
    # HELP
    # --------------------------------

    elif user == "help":

        print()
        print("========== CHATBOT HELP ==========")
        print("You can ask me:")
        print()
        print("1. Hello")
        print("2. How are you?")
        print("3. What is your name?")
        print("4. My name is John")
        print("5. Who created you?")
        print("6. What is Python?")
        print("7. Tell me a joke")
        print("8. Give me study tips")
        print("9. Help me with exams")
        print("10. What is the time?")
        print("11. What is today's date?")
        print("12. I am happy")
        print("13. I am sad")
        print("14. Thank you")
        print("15. Bye")
        print("===================================")
        print()


    # --------------------------------
    # BYE / EXIT
    # --------------------------------

    elif user == "bye" or user == "goodbye" or user == "exit" or user == "quit":

        print("Bot: Goodbye!")
        print("Bot: Thanks for chatting with me.")
        print("Bot: Have a great day!")
        break
    else:

        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see what I can answer.")

    print()
    print("Chatbot program closed.")