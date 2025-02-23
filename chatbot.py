import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! Need any help?"]],
    
    [r"how are you?", ["I'm just a chatbot, but I'm doing well!", "I'm great! How about you?"]],
    
    [r"what is your name?", ["I'm your friendly chatbot assistant!", "You can call me ChatBot."]],
    
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]],
    
    [r"where is my order?", ["Please provide your order number, and I’ll check for you.", 
                              "I can track your order. What’s your order number?"]],
    
    [r"recommend me a laptop", ["Are you looking for a gaming, business, or budget laptop?", 
                                "What’s your budget range? I can suggest something accordingly."]],
    
    [r"what is the return policy?", ["Our return policy allows returns within 30 days. More details at: [link]",
                                     "You can return products within 30 days if they meet our conditions."]],
    
    [r"thank you", ["You're welcome!", "Glad I could help!", "Anytime!"]],
    
    [r".*", ["I'm sorry, I didn't understand that. Could you please rephrase?", 
             "Hmm, I'm not sure about that. Would you like me to connect you with a human agent?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start chatbot
print("Chatbot: Hello! I am here to assist you. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)