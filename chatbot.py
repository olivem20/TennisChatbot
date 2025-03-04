# Import necessary modules
import nltk
import re
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?",]],
    [r"hi|hey|hello", ["Hello, how can I help you?", "Hey there! What can I do for you?", "Hi! How can I assist you today?"]],
    [r"what is your name?", ["I am a chatbot created to assist you. You can call me Chatbot.",]],
    [r"how are you?", ["I'm a bot, so I don't have feelings, but I'm here to help you!",]],
    [r"can you help me with (.*)", ["Sure, I can help you with %1. Please provide more details.",]],
    [r"sorry (.*)", ["It's okay. How can I assist you?",]],
    [r"thank you|thanks", ["You're welcome!", "No problem!", "Happy to help!"]],


    # Forehands
    [r"how (.*) forehand", [
        "You can break the forehand down into 4 simple steps:\n "
        "1) Get your shoulders and feet sideways to the net\n"
        "2) Put your racket in your right hand and get it back abd below on the right side of your body\n"
        "3) Put your left arm out in front of you at a 45° angle\n"
        "4) Swing low to high, catch your racket with your left hand and follow through over your left shoulder!\n"
        "Congrats, now you know how to hit a forehand!\n"
    ]],

    [r"(.*) forehand grip (.*)| (.*) grip (.*) forehand (.*)", [
        "To get the correct grip for a beginner forehand, you must put your index knuckle on the thick, flat side of the grip and hold it comfortably"
        "so that when you get your racket back, the face of the racket is perpindicular to the ground."
    ]],

    # Backhand
    [r"how (.*) backhand", [
        "Let's break down the backhand into simpler steps so it's easy to understand!:\n "
        "1) Get your shoulders and feet sideways to the net\n"
        "2) Hold the racket with your right hand like your shaking hands with it or hammering a nail\n"
        "3) Put your left hand on top of your right hand, with the left index knuckle on the fat, flat side of the grip\n"
        "4) Put your racket back and below by your left hip!\n"
        "5) Swing from low to high, feeling your left hand doing most of the work and follow through over your right shoulder!\n"
        "Congrats, now you know how to hit a basic backhand :)"
    ]],

    # Serve
    [r"how (.*) serve", [
        "Serves are one of the hardest shots in tennis! For this serve, make sure you are holding the racket using a forehand grip." 
        "Here are some basic steps to start learning a serve:\n"
        "1) Face the net with your feet at shoulder width, standing an inch behind the baseline\n"
        "2) Take a step back with your right foot and make sure you are balanced\n"
        "3) Hold the ball in your left hand, and rest your racket up over your right shoulder\n"
        "4) Toss the ball up in front of you, make contact at the highest point of your toss and follow through to your target!\n"
        "Congrats! You now know how to hit a beginner serve :)"
    ]],

    # Volleys
    [r"how (.*) (volley|volleys)", [
        "To start learning volleys, lets keep it very simple!\n"
        "For both volleys you want to keep a very short swing, it should almost feel like your punching the ball!\n"
        "For a FH volley, keep your forehand grip and make a 90° angle with your right elbow. Kepp your eye on the ball and punch the ball towards your target.\n"
        "For a BH volley, keep the same idea. Use your two handed backhand grips and punch the ball towards your target but letting your left hand guide the shot.\n"
        "You now know how to hit volleys as a beginner!"
    ]],

    # Other
    [r"can you help me with (.*)", ["Sure, I can help you with %1 in tennis. Please provide more details.",]],
    [r"sorry (.*)", ["It's okay. How can I assist you with tennis?",]],
    [r"quit", ["Bye! Keep improving your game!", "Goodbye! See you on the court!"]],
    [r"(.*)", ["I'm sorry, I don't understand that. Can you rephrase?", "Could you please elaborate on that?"]]
    
]

# Define the chatbot class
class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)

# Initialize the chatbot
chatbot = RuleBasedChatbot(pairs)

# Function to chat with the bot
def chat_with_bot():
    print("🎾Hi, I'm your AI Tennis Coach! What can I help you with? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Keep improving your game! 🎾")
            break
        response = chatbot.respond(user_input)
        print(f"Coach: {response}")

# Start chatting with the bot
chat_with_bot()
