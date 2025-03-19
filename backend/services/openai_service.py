import openai
import os
from fastapi import UploadFile
import base64

# Initialize OpenAI client with API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def extract_dice_from_image(image: UploadFile) -> str:
    """
    Use GPT Vision to extract dice text from the image.
    """
    image_bytes = await image.read()
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Clearly identify the text visible on each dice in this image."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ],
            }
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()

def get_recipe_from_dice(dice_description: str) -> str:
    """
    Generate recipe using GPT-4 based on dice description.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a culinary assistant creating recipes based on ingredients and cuisines."},
            {"role": "user", "content": f"Generate a recipe using these dice results: {dice_description}"}
        ],
        max_tokens=500,
    )

    return response.choices[0].message.content.strip()

def generate_recipe_image(recipe: str) -> str:
    """
    Generate a recipe image using DALL·E.
    """
    prompt = f"Professional, appetizing food photography of the dish described here: {recipe}"

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    return response.data[0].url
