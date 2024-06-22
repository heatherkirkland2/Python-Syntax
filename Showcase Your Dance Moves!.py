#1. Showcase Your Dance Moves!
#Python Indentation Practice with if Statements

#Objective: The aim of this assignment is to understand the importance of indentation in Python, especially with if statements.

#Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")



#Task 2: Your Mood Today Ask the user how they feel today. If they say "happy", print "That's great to hear!",
#and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented.

#By the end of this assignment, you should feel more confident about how 
#if statements work in Python and how to indent them properly.

# Ask the user how they feel
user_mood = input("How do you feel today? ")

# Check their response
if user_mood.lower() == "happy":
    print("That's great to hear!")
elif user_mood.lower() == "sad":
    print("I hope your day gets better!")
else:
    print("Hmm, I'm not sure how to respond. 🤔")

