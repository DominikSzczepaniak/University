import React from 'react';
import Education from "../components/Education";
import Experience from "../components/Experience";
import Skill from "../components/Skill";

const AboutMe = () => {
    const experienceData1 = {
        imgSource: "../public/techinnovation.png",
        companyName: "Tech Innovations",
        role: "Front-end Developer",
        description: "Worked as a part of a dynamic team to deliver modern web applications using cutting-edge technologies.",
        responsibilities: [
            "Developed interactive UI components using React",
            "Implemented responsive web designs using CSS and JavaScript",
            "Collaborated with back-end developers to integrate APIs"
        ],
        technologies: ["react", "css", "javascript"],
        startDate: "January 2020",
        endDate: "Current",
        city: "Wrocław"
    };


    const experienceData2 = {
        imgSource: "../public/googlelogo.png",
        companyName: "Google",
        role: "Front-end Developer",
        description: "Worked as a part of a dynamic team to deliver modern web applications using cutting-edge technologies.",
        responsibilities: [
            "Developed interactive UI components using React",
            "Implemented responsive web designs using CSS and JavaScript",
            "Collaborated with back-end developers to integrate APIs"
        ],
        technologies: ["react", "css", "javascript"],
        startDate: "January 2019",
        endDate: "January 2020",
        city: "Wrocław"
    };

    const educationData1 = {
        logoUrl: "../public/uwrlogo.png",
        schoolName: "University of Wrocław",
        location: "Wrocław, Dolnośląskie, Poland",
        achievements: ["FCE certificate, Score 177"],
        startDate: "2022",
        endDate: "2026"
    };

    const description = "I am a front-end developer with 2 years of experience in building modern web applications. I am passionate about creating user-friendly and visually appealing websites. I have a strong understanding of web technologies and a keen eye for design. I am always eager to learn new things and improve my skills."

    return (
        <div className="min-h-screen bg-gray-400 flex justify-center items-center p-4">
            <div className="container mx-auto bg-white shadow-xl rounded-lg p-8">
                <img src="../public/avatar.jpg" alt="Avatar" className="h-24 w-24 rounded-full mx-auto mb-4" />
                <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">About Me</h1>
                <p className="text-lg text-gray-700 mb-4">{description}</p>
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">Education</h2>
                <div className="flex flex-wrap justify-center gap-4 mb-8">
                    <Education {...educationData1} />
                </div>
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">Experience</h2>
                <Experience {...experienceData1} />
                <Experience {...experienceData2} />
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">Skills</h2>
                <div className="flex gap-2 flex-wrap">
                    <Skill name="JavaScript" />
                    <Skill name="React" />
                    <Skill name="TypeScript" />
                </div>
            </div>
        </div>
    );
};

export default AboutMe;
