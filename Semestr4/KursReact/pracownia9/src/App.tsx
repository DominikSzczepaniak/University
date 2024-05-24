import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Question from './components/Question';
import Loading from './components/Loading';

interface Item {
  id: string;
  attributes: {
    name: string;
    effect: string;
  };
}

const App: React.FC = () => {
  const [spells, setSpells] = useState<Item[]>([]);
  const [potions, setPotions] = useState<Item[]>([]);
  const [currentCategory, setCurrentCategory] = useState<'spells' | 'potions' | null>(null);
  const [currentQuestion, setCurrentQuestion] = useState<number>(0);
  const [score, setScore] = useState<number>(0);
  const [highScore, setHighScore] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if(spells.length === 0 && potions.length === 0){
          const spellsResponse = await axios.get('https://api.potterdb.com/v1/spells');
          const potionsResponse = await axios.get('https://api.potterdb.com/v1/potions');
          setSpells(spellsResponse.data.data);
          setPotions(potionsResponse.data.data);
          setLoading(false);
        }
      } catch (err) {
        setError('Failed to fetch data from PotterDB');
        setLoading(false);
      }
    };

    fetchData();
    const storedHighScore = localStorage.getItem('highScore');
    if (storedHighScore) {
      setHighScore(parseInt(storedHighScore, 10));
    }
  }, []);

  const handleAnswer = (isCorrect: boolean) => {
    if (isCorrect) {
      const newScore = score + 1;
      setScore(newScore);
      if (newScore > highScore) {
        setHighScore(newScore);
        localStorage.setItem('highScore', newScore.toString());
      }
      setCurrentQuestion((prevQuestion) => prevQuestion + 1);
    } else {
      setScore(0);
    }
  };

  const handleCategorySelection = (category: 'spells' | 'potions') => {
    setCurrentCategory(category);
    setCurrentQuestion(0);
    setScore(0);
  };

  const handleNextQuestion = () => {
    setCurrentQuestion((prevQuestion) => prevQuestion + 1);
  };

  if (loading) return <Loading />;
  if (error) return <div className="text-red-500">{error}</div>;

  if (!currentCategory) {
    return (
      <div className="container mx-auto p-4 bg-gray-300 w-6/12">
        <h1 className="text-3xl font-bold text-center">Harry Potter Guessing Game</h1>
        <div className="text-center">High Score: {highScore}</div>
        <div className="flex justify-center space-x-4 mt-8">
          <button
            className="p-2 bg-blue-500 text-white rounded"
            onClick={() => handleCategorySelection('spells')}
          >
            Spells
          </button>
          <button
            className="p-2 bg-green-500 text-white rounded"
            onClick={() => handleCategorySelection('potions')}
          >
            Potions
          </button>
        </div>
      </div>
    );
  }

  const data = currentCategory === 'spells' ? spells : potions;
  const currentItem = data[currentQuestion];

  if (!currentItem) {
    return (
      <div className="container mx-auto p-4 bg-gray-300 w-6/12">
        <h1 className="text-3xl font-bold text-center">Harry Potter Guessing Game</h1>
        <div className="text-center">High Score: {highScore}</div>
        <div className="text-center">
          You've completed all the questions in the {currentCategory} category!
        </div>
        <div className="flex justify-center space-x-4 mt-8">
          <button
            className="p-2 bg-blue-500 text-white rounded"
            onClick={() => setCurrentCategory(null)}
          >
            Choose different category
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4 bg-gray-300 w-6/12">
      <h1 className="text-3xl font-bold text-center">Harry Potter Guessing Game</h1>
      <div className="text-center">High Score: {highScore}</div>
      <p className="text-center">Score: {score}</p>
      <Question
        item={currentItem}
        items={data}
        onAnswer={handleAnswer}
        onNextQuestion={handleNextQuestion}
        key={currentItem.id}
      />
    </div>
  );
};

export default App;
