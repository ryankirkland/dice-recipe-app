from fastapi import APIRouter, UploadFile, File, HTTPException
from services.openai_service import (
    extract_dice_from_image,
    get_recipe_from_dice,
    generate_recipe_image,
)

router = APIRouter()

@router.post("/generate-recipe")
async def generate_recipe(image: UploadFile = File(...)):
    """
    Endpoint to handle dice image upload, extract dice text,
    generate a recipe with GPT-4, and an image with DALL·E.
    """
    # Ensure the file is an image
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type.")

    # Step 1: Extract dice information using GPT Vision
    dice_description = await extract_dice_from_image(image)

    # Step 2: Generate recipe based on dice description
    recipe = get_recipe_from_dice(dice_description)

    # Step 3: Generate matching recipe image via DALL·E
    recipe_image_url = generate_recipe_image(recipe)

    # Step 4: Return recipe text and image URL to frontend
    return {
        "dice_results": dice_description,
        "recipe": recipe,
        "recipe_image_url": recipe_image_url
    }
