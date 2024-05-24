import React from 'react';

interface ProjectProps {
  name: string;
  technologies: string[];
  description: string;
  codeUrl: string;
}

const Project: React.FC<ProjectProps> = ({ name, technologies, description, codeUrl }) => {
  return (
    <div className="bg-white p-6 shadow-lg rounded-lg mb-6">
      <h3 className="text-xl font-semibold text-gray-800 mb-2">{name}</h3>
      <p className="text-gray-700 mb-4">{description}</p>
      <div className="flex flex-wrap items-center gap-2 mb-4">
        {technologies.map((tech, index) => (
          <span key={index} className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded">
            {tech}
          </span>
        ))}
      </div>
      <a href={codeUrl} className="text-blue-500 hover:text-blue-700 font-bold">View Code</a>
    </div>
  );
};

export default Project;
