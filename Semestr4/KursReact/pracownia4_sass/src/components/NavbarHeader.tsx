import styles from "./NavbarHeader.module.scss"

interface NavbarHeaderProps{
    darkMode: boolean;
    setDarkMode: (darkMode: boolean) => void;
    name: string;
    slogan: string;
}

function NavbarHeader(props: NavbarHeaderProps){
    const { darkMode, setDarkMode, name, slogan } = props;
    const toggleTheme = () => {
        setDarkMode(!darkMode);
    };
    return (
        <>
        <div className="navbar">
            <a href="#header">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#team">Team</a>
            <a href="#blog">Blog</a>
            <a href="#contact">Contact</a>
            <button onClick={toggleTheme} className="theme-toggle-button">
                {darkMode ? "Light Mode" : "Dark Mode"}
            </button>
        </div>
            <header id="header" className="header">
            <div className="header-content">
                <h1>{name}</h1>
                <p>{slogan}</p>
            </div>
        </header>
        </>
    );
}

export default NavbarHeader;