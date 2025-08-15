import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# --- 1. Load API Key ---
# This line loads the environment variables from your .env file
load_dotenv()

# This configures the Google AI library with your secret API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# --- 2. Function to Get Image Description ---
def get_image_caption(image_path, prompt):
    """
    Sends an image and a prompt to the Gemini model and returns the text response.
    """
    print("Loading model...")
    # We use the 'gemini-pro-vision' model because it can understand images
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("Opening image...")
    # Opens the image file
    input_image = Image.open(image_path)

    print("Asking the AI for a caption...")
    # The 'generate_content' method sends the data to the AI
    # We send a list containing both our text prompt and the image
    response = model.generate_content([prompt, input_image])

    return response.text


# --- 3. Main Execution Block ---
if __name__ == "__main__":
    # Define the path to the image you want to describe
    # Make sure this image file exists in your project folder!
    image_file_path = "test_image.jpg"

    # The prompt tells the AI what you want it to do
    user_prompt = "Describe this image in a single, descriptive sentence."

    # Call our function and print the result
    try:
        caption = get_image_caption(image_file_path, user_prompt)
        print("\n🤖 AI Caption:")
        print(caption)
    except FileNotFoundError:
        print(f"Error: The file '{image_file_path}' was not found.")
        print("Please make sure you have an image with that name in your project folder.")