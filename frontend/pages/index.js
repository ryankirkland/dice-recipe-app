import { useState } from 'react';
import ImageUploader from '../components/ImageUploader';
import RecipeCard from '../components/RecipeCard';

export default function Home() {
  const [recipeData, setRecipeData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleUpload = async (formData) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/api/generate-recipe', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Network response was not ok');

      const data = await response.json();
      setRecipeData(data);
    } catch (err) {
      console.error(err);
      setError('An error occurred while generating the recipe.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#faf7f2] py-14 px-4">
      <div className="text-center mb-10">
        <h1 className="text-5xl font-bold text-gray-800 mb-3">🎲 AI Dice Recipe Generator</h1>
        <p className="text-gray-600 text-lg">
          Roll the dice, snap a photo, and let the culinary magic happen!
        </p>
      </div>

      <div className="max-w-md mx-auto bg-white rounded-xl shadow-lg p-6 mb-8">
        <ImageUploader onUpload={handleUpload} />
      </div>

      {loading && <p className="text-center text-lg">Cooking up your recipe... 🍳</p>}
      {error && <p className="text-center text-red-500 text-lg">{error}</p>}

      {recipeData && (
        <div className="mt-10">
          <RecipeCard
            diceResults={recipeData.dice_results}
            recipe={recipeData.recipe}
            recipeImageUrl={recipeData.recipe_image_url}
          />
        </div>
      )}
    </div>
  );
}
