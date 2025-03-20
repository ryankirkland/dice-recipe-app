import { motion } from 'framer-motion';

export default function RecipeCard({ diceResults, recipe, recipeImageUrl }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, ease: "easeOut" }}
      className="max-w-4xl mx-auto p-10 rounded-3xl shadow-2xl bg-white"
    >
      <img
        src={recipeImageUrl}
        alt="Recipe"
        className="rounded-2xl mb-6 shadow-md object-cover h-[400px] w-full"
      />
      <h2 className="text-3xl font-bold mb-2 text-gray-800">Your Culinary Creation</h2>
      <p className="italic mb-6 text-gray-600">Ingredients: {diceResults}</p>
      <div className="text-gray-700 whitespace-pre-line leading-relaxed">{recipe}</div>
    </motion.div>
  );
}


  
  