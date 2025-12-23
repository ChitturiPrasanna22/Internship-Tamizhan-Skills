#  Shopping Mall Chatbot 

# Predefined responses
responses = {
    "hello": "Hello! Welcome to Grand Plaza Mall. How can I assist you today?",
    "hi": "Hi there! Looking for something in the mall?",
    "timings": "Our mall is open from 10 AM to 10 PM every day.",
    "food court": "The food court is located on the 2nd floor near the central atrium.",
    "parking": "We have parking available for 500 cars in the basement.",
    "cinema": "Our multiplex cinema is on the 3rd floor. Movies start every 30 minutes.",
    "stores": "We have apparel, electronics, and lifestyle stores. Any specific category you are looking for?",
    "restroom": "Restrooms are available on every floor near the elevators.",
    "thank you": "You're welcome! Enjoy your visit.",
    "ok":"okay thank you ",
    "bye": "Goodbye! Have a great day at Grand Plaza Mall!"
}

# Default response if no pattern matches
default_response = "I'm sorry, I didn't understand that. Can you rephrase?"

#  Preprocess Input 
def preprocess(text):
    return text.lower().strip()

# Get Response 
def get_response(user_input):
    user_input = preprocess(user_input)
    for key in responses:
        if key in user_input:  # simple pattern matching
            return responses[key]
    return default_response

#  Main Loop 
print("Welcome to the Grand Plaza Mall Assistant!")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day at Grand Plaza Mall!")
        break

    reply = get_response(user_input)
    print("Bot:", reply)
