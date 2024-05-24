import React from 'react';

interface SkillProps {
  name: string;
}

const Skill: React.FC<SkillProps> = ({ name }) => {
  return (
    <div className="border border-blue-500 text-blue-500 py-1 px-3 rounded-full text-sm font-medium">
      {name}
    </div>
  );
};

export default Skill;
