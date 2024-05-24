import React, { useState } from 'react';

interface Item {
  id: string;
  attributes: {
    name: string;
    effect: string;
  };
}

interface QuestionProps {
  item: Item;
  items: Item[];
  onAnswer: (isCorrect: boolean) => void;
  onNextQuestion: () => void;
}

const Question: React.FC<QuestionProps> = ({ item, items, onAnswer, onNextQuestion }) => {
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<string | null>(null);
  const showCorrect = true;

  const shuffledItems = [...items].sort(() => 0.5 - Math.random());
  const options = [item, ...shuffledItems.slice(0, 3)].sort(() => 0.5 - Math.random());

  const handleAnswer = (answer: string) => {
    setSelectedAnswer(answer);
    if (answer === item.attributes.name) {
      setFeedback('Correct!');
      onAnswer(true);
    } else {
      setFeedback('Incorrect! Try again.');
      onAnswer(false);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-4 shadow-md rounded-md">
      <p className="text-xl mb-4">What has the following effect?</p>
      <p className="mb-6 italic">"{item.attributes.effect}"</p>
      <div className="grid grid-cols-2 gap-4">
        {options.map((option) => (
          <button
            key={option.id}
            className={`p-2 text-white rounded ${
              option.attributes.name === item.attributes.name && showCorrect
                ? 'bg-green-500'
                : 'bg-blue-500'
            }`}
            onClick={() => handleAnswer(option.attributes.name)}
            disabled={!!selectedAnswer}
          >
            {option.attributes.name}
          </button>
        ))}
      </div>
      {feedback && (
        <div className="mt-4">
          <p className={`mb-4 ${feedback === 'Correct!' ? 'text-green-500' : 'text-red-500'}`}>
            {feedback}
          </p>
          {feedback === 'Incorrect! Try again.' && (
            <button
              className="p-2 bg-blue-500 text-white rounded"
              onClick={onNextQuestion}
            >
              Next Question
            </button>
          )}
        </div>
      )}
    </div>
  );
};

export default Question;
