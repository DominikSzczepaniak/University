import React, { useState } from 'react';
import { useRecipes } from '../RecipeContext';
import './RecipeList.css'; 

export const RecipeList = () => {
  const {state: recipes, dispatch} = useRecipes();
  const [searchTerm, setSearchTerm] = useState('');
  const [showOnlyFavorites, setShowOnlyFavorites] = useState(false); 

  const toggleShowFavorites = () => {
    setShowOnlyFavorites(!showOnlyFavorites);
  };

  const filteredRecipes = recipes.filter(recipe =>
    (recipe.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    recipe.content.toLowerCase().includes(searchTerm.toLowerCase())) &&
    (!showOnlyFavorites || recipe.isFavorite) 
  );

  return (
    <div className="recipeList">
      <input
        type="text"
        placeholder="Szukaj przepisów..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="searchInput"
      />
      <button onClick={toggleShowFavorites} className="filterFavoritesButton">
        {showOnlyFavorites ? 'Pokaż wszystkie' : 'Pokaż ulubione'}
      </button>
      {filteredRecipes.length > 0 ? (
        filteredRecipes.map(recipe => (
          <div className="recipeItem" key={recipe.id}>
            <h3>{recipe.name} {recipe.isFavorite && '❤️'}</h3>
            <p>{recipe.content}</p>
            <div className="recipeActions">
              <button 
                onClick={() => dispatch({ type: 'TOGGLE_FAVORITE', data: { id: recipe.id } })}
                className="toggleFavoriteButton">
                Ulubione
              </button>
              <button 
                onClick={() => dispatch({ type: 'REMOVE', data: { id: recipe.id } })}
                className="removeRecipeButton">
                Usuń
              </button>
            </div>
          </div>
        ))
      ) : (
        <p>Brak przepisów do wyświetlenia.</p>
      )}
    </div>
  );
};
