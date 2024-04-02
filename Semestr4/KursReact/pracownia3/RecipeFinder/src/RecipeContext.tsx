import React, { createContext, useReducer, useContext } from 'react';

interface Recipe {
  id: string;
  name: string;
  content: string;
  isFavorite: boolean;
}

type RecipeState = Recipe[];

type RecipeAction =
  | { type: 'ADD'; data: Recipe }
  | { type: 'REMOVE'; data: { id: string } }
  | { type: 'TOGGLE_FAVORITE'; data: { id: string } };

type ContextType = { state: RecipeState; dispatch: React.Dispatch<RecipeAction> };

const defaultContextValue = {
  state: [],
  dispatch: () => null
};

const RecipeContext = createContext<ContextType>(defaultContextValue);

function recipeReducer(state: RecipeState, action: RecipeAction): RecipeState {
  switch (action.type) {
    case 'ADD':
      return [...state, action.data];
    case 'REMOVE':
      return state.filter(recipe => recipe.id !== action.data.id);
    case 'TOGGLE_FAVORITE':
      return state.map(recipe =>
        recipe.id === action.data.id ? { ...recipe, isFavorite: !recipe.isFavorite } : recipe
      );
    default:
      return state;
  }
}

export const RecipeProvider = ({ children }: { children: React.ReactNode }) => {
  const [state, dispatch] = useReducer(recipeReducer, []);

  return (
    <RecipeContext.Provider value={{ state, dispatch }}>
      {children}
    </RecipeContext.Provider>
  );
};

export const useRecipes = () => useContext(RecipeContext);
