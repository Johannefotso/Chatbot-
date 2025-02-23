<b> Introduction <br> </b>
This chatbot is an example of how to use Natural Language Processing (NLP) to create a basic conversation assistant. It recognizes patterns in user input and responds accordingly.

<b> Features <br> </b>
✅ Greeting Users – Responds to "hi", "hello", etc. <br>
✅ Order Tracking – Asks for an order number to simulate tracking <br>
✅ Product Recommendations – Suggests laptops based on user preferences <br>
✅ FAQ Handling – Provides basic responses to common queries <br>
✅ Error Handling – Responds to unrecognized inputs with a default message <br>

<b> Installation <br> </b>
1️⃣ Requirements <br>
Python 3.x (Check with python3 --version) <br>
pip installed (Check with python3 -m ensurepip --default-pip)<br>

<b> 2️⃣ Install Dependencies <br> </b>
Run the following command: <br>
<br>
<i> python3 -m pip install nltk<br> </i> 
<br> 
Then, open Python and download NLP data:<br>
<br> <i>
import nltk <br>
nltk.download('punkt') <br>
</i> <br>
<b> Example Conversation <br> </b>
Chatbot: Hello! How can I assist you today? <br>
You: hi <br>
Chatbot: Hello! Need any help? <br>
You: where is my order? <br>
Chatbot: Please provide your order number, and I’ll check for you. <br>
You: recommend me a laptop <br>
Chatbot: Are you looking for a gaming, business, or budget laptop? <br>
You: bye <br>
Chatbot: Goodbye! Have a great day! <br>
