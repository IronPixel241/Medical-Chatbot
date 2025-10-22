import google.generativeai as genai

# Replace this with your actual Gemini API key
genai.configure(api_key="AIzaSyBt8_aMRTTg2xyJOBbGe5cDNkEpbryUHhY")

# List all available models
for model in genai.list_models():
    print(model.name)
