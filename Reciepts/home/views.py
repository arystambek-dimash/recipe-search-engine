from django.shortcuts import render
import openai,os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_KEY",None)
# Create your views here.
def home(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')

        if "food" in user_input.lower():
            prompt = f"Answer when asked about food. How to make {user_input} recipe? Or provide the most tasty food options when the user writes the ingredients."
        else:
            prompt = "Sorry, I can only provide recipes for food."

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=156,
            temperature=0.5
        )
        chatbot_response = response["choices"][0]["text"]

    return render(request, 'home/index.html', {"response": chatbot_response})