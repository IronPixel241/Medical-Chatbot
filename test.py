import google.generativeai as genai

# Replace this with your actual Gemini API key

# List all available models
for model in genai.list_models():
    print(model.name)
