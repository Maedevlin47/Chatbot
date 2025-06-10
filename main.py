import openai
from openai import AuthenticationError, RateLimitError, APIConnectionError, OpenAIError

# Set your OpenAI API key
openai.api_key = "sk-proj-..."  # ← keep your key here

# Define the chatbot's prompt
prompt = "Answer questions about fashion, events, skincare, makeup, brands, home goods, and restaurants in the United States."

# Ask user for input
user_input = input("Ask me anything: ")

# Add try/except block properly
try:
    # Make the API request
    response = openai.ChatCompletion.create(
        model="gpt-4.o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract and print the AI's response
    answer = response["choices"][0]["message"]["content"]
    print("\nAssistant:", answer)

except AuthenticationError:
    print("❌ Invalid or missing API key.")
except RateLimitError:
    print("⚠️ Too many requests. Try again later.")
except APIConnectionError:
    print("❌ Network error. Please check your internet connection.")
except OpenAIError as e:
    print(f"⚠️ OpenAI error: {e}")
except Exception as e:
    print(f"🚨 Unexpected error: {e}")