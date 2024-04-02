import React from 'react';
import { RecipeProvider } from './RecipeContext';
import { AddRecipe } from './components/AddRecipe';
import { RecipeList } from './components/RecipeList';

function App() {
  return (
    <RecipeProvider>
      <div className="App">
        <h1 style={{ textAlign: 'center', margin: '20px 0' }}>Wyszukiwarka przepisów</h1>
        <AddRecipe />
        <RecipeList />
      </div>
    </RecipeProvider>
  );
}

export default App;
