import random

#Responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! Need help with something?"],
    "order_status": ["Please provide your order number.", "I can check that for you! What’s your order number?"],
    "product_recommendation": ["Are you looking for a laptop, phone, or another gadget?", "What’s your budget? I can suggest something based on that."],
    "return_policy": ["Our return policy allows returns within 30 days. You can find more details here: [link]"],
    "unknown": ["I'm sorry, I didn't understand that. Could you please rephrase?", "Hmm, I’m not sure. Let me connect you to a human agent."]
}

#User Input
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input:
        return random.choice(responses["greeting"])
    elif "order" in user_input:
        return random.choice(responses["order_status"])
    elif "recommend" in user_input or "laptop" in user_input:
        return random.choice(responses["product_recommendation"])
    elif "return" in user_input:
        return random.choice(responses["return_policy"])
    else:
        return random.choice(responses["unknown"])

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you for visiting TechStore Support. Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
