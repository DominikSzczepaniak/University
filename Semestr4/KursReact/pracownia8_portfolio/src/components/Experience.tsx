import React from 'react';

interface ExperienceDataProps {
  imgSource: string;
  companyName: string;
  role: string;
  description: string;
  responsibilities: string[];
  technologies: string[];
  startDate: string;
  endDate: string;
  city: string;
}

function Experience(props: ExperienceDataProps) {
  return (
    <div className="bg-zinc-300 shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div className="flex items-center space-x-4 mb-6">
        <img src={props.imgSource} alt="Logo firmy" className="h-12 w-12" />
        <div>
          <p className="text-xl font-bold">{props.companyName}</p>
          <p className="text-sm text-gray-600">{props.role}</p>
        </div>
      </div>

      <hr className="mb-6" />

      <p className="mb-4">{props.description}</p>
      <p className="font-bold mb-2">Moje obowiązki:</p>
      <ul className="list-disc pl-5 mb-4">
        {props.responsibilities.map((responsibility, index) => (
          <li key={index} className="text-gray-700">{responsibility}</li>
        ))}
      </ul>

      <p className="font-bold mb-2">Używane technologie:</p>
      <div className="flex flex-wrap items-center gap-2 mb-4">
        {props.technologies.map((tech, index) => (
          <span key={index} className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded">
            {tech}
          </span>
        ))}
      </div>

      <p className="text-gray-600">{props.startDate} - {props.endDate} | {props.city}</p>
    </div>
  )
}

export default Experience;
