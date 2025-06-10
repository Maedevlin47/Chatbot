import os
from openai import OpenAI, OpenAIError, APIConnectionError, RateLimitError, APIStatusError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("Loaded key:", repr(api_key))  # For debugging

# Initialize the client
client = OpenAI(api_key=api_key)

# Define prompt
prompt = "Answer questions about fashion, events, skincare, makeup, brands, home goods, and restaurants in the United States."

# Get user input
user_input = input("Ask me anything: ")

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print("\nAssistant:", response.choices[0].message.content)

except APIStatusError as e:
    print("❌ Invalid or missing API key.")
    print("Details:", e)
except RateLimitError:
    print("⚠️ Too many requests. Try again later.")
except APIConnectionError:
    print("❌ Network error. Please check your internet connection.")
except OpenAIError as e:
    print(f"⚠️ OpenAI error: {e}")
except Exception as e:
    print(f"🚨 Unexpected error: {e}")


