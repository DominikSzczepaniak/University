import React from 'react';

interface EducationProps {
  logoUrl: string;
  schoolName: string;
  location: string;
  achievements: string[];
  startDate: string;
  endDate: string;
}   

function Education(props: EducationProps) {
  return (
    <div className="flex flex-col bg-zinc-300 shadow-md rounded-lg p-4 mb-4 w-full md:w-1/2 lg:w-1/3">
      <div className="flex items-center space-x-4 mb-4">
        <img src={props.logoUrl} alt="Logo szkoły" className="h-12 w-12" />
        <div>
          <p className="text-lg font-bold">{props.schoolName}</p>
          <p className="text-sm text-gray-600">{props.location}</p>
        </div>
      </div>

      <hr className="mb-4" />

      <ul className="list-disc pl-5 mb-4">
        {props.achievements.map((achievement, index) => (
          <li key={index} className="text-gray-700">{achievement}</li>
        ))}
      </ul>

      <p className="text-gray-600">{props.startDate} - {props.endDate}</p>
    </div>
  );
}

export default Education;
