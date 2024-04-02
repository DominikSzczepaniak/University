import React, { useState } from 'react';
import { useRecipes } from '../RecipeContext';
import { v4 as uuidv4 } from 'uuid';
import './addRecipe.css';

export const AddRecipe = () => {
  const { dispatch } = useRecipes();
  const [name, setName] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    dispatch({ type: 'ADD', data: { id: uuidv4(), name, content, isFavorite: false } });
    setName('');
    setContent('');
  };

  return (
    <form className="addRecipeForm" onSubmit={handleSubmit}>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Nazwa przepisu" />
      <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Treść przepisu"></textarea>
      <button type="submit">Dodaj przepis</button>
    </form>
  );
};
