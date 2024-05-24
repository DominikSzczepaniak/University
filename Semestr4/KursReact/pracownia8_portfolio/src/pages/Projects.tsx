import Project from '../components/Project';

const Projects = () => {
    return (
        <div className="p-8">
            {/* <h1 className="text-3xl text-white font-bold text-center mb-6">My Projects</h1> */}
            <Project
                name="Project Alpha"
                technologies={['React', 'Tailwind CSS', 'Firebase']}
                description="This project is a web application designed to demonstrate modern web development practices using React and Tailwind CSS."
                codeUrl="https://github.com/example/project-alpha"
            />
            <Project
                name="Project Beta"
                technologies={['Next.js', 'TypeScript', 'GraphQL']}
                description="This project is a full-stack web application built with Next.js, TypeScript, and GraphQL."
                codeUrl=""
            />
            <Project
                name="Project Gamma"
                technologies={['Node.js', 'Express', 'MongoDB']}
                description="This project is a RESTful API built with Node.js, Express, and MongoDB."
                codeUrl=""
            />
            <Project
                name="Project Delta"
                technologies={['Vue.js', 'Vuetify', 'Firebase']}
                description="This project is a web application built with Vue.js and Vuetify."
                codeUrl=""
            />
            <Project 
                name="Project Epsilon"
                technologies={['Angular', 'Bootstrap', 'Firebase']}
                description="This project is a web application built with Angular and Bootstrap."
                codeUrl=""
            />

        </div>
    );
};

export default Projects;
