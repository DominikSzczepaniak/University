const Home = () => {
    const opis = "Jestem pasjonatem technologii i junior developerem, który specjalizuje się w tworzeniu nowoczesnych aplikacji webowych. Obecnie jestem studentem Uniwersytetu Wrocławskiego na kierunku Informatyka, gdzie zgłębiam swoje umiejętności programistyczne i techniczne."

    return (
        <div className="min-h-screen">
            <div className="bg-white p-10 shadow-lg rounded-lg max-w-screen-md mx-auto mt-10">
                <img src="../public/avatar.jpg" alt="Zdjęcie profilowe" className="rounded-full w-32 h-32 mx-auto mb-6" />
                <h1 className="text-3xl text-center font-bold mb-4">Cześć, nazywam się Dominik</h1>
                <h2 className="text-xl text-center mb-5">{opis}</h2>
                <ul className="flex justify-center space-x-4">
                    <li><a href="https://github.com/" className="text-blue-500 hover:text-blue-700">GitHub</a></li>
                    <li><a href="https://linkedin.com/in/" className="text-blue-500 hover:text-blue-700">LinkedIn</a></li>
                    <li><a href="mailto:twój_email@example.com" className="text-blue-500 hover:text-blue-700">Email</a></li>
                </ul>
            </div>
        </div>
    );
};

export default Home;
