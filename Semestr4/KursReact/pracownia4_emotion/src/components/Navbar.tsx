import React from "react";
import { css } from "@emotion/react";
import { useTheme } from "@emotion/react";

interface NavbarProps {
  darkMode: boolean;
  setDarkMode: (darkMode: boolean) => void;
}

type themeType = {
  background: string;
  text: string;
  navbarBackground: string;
  contentCardBackground: string;
  buttonLightBackground: string;
  buttonHoverLightBackground: string;
};

const Navbar: React.FC<NavbarProps> = (props) => {
  const { darkMode, setDarkMode } = props;
  const theme = useTheme()

  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div
      css={css`
        position: sticky;
        top: 0;
        padding: 10px 0;
        text-align: center;
        z-index: 1000;
        background-color: ${theme.navbarBackground};
      `}
    >
      <a
        href="#header"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        Home
      </a>
      <a
        href="#about"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        About
      </a>
      <a
        href="#services"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        Services
      </a>
      <a
        href="#team"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        Team
      </a>
      <a
        href="#blog"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        Blog
      </a>
      <a
        href="#contact"
        css={css`
          text-decoration: none;
          padding: 0 20px;
          color: ${theme.text};
        `}
      >
        Contact
      </a>
      <button
        onClick={toggleTheme}
        css={css`
          cursor: pointer;
          padding: 10px 20px;
          transition: background-color 0.3s ease;
          background-color: ${theme.buttonBackground};
          color: ${theme.buttonText};
          &:hover {
            background-color: ${theme.buttonHoverBackground};
          }
        `}
      >
        {darkMode ? "Light Mode" : "Dark Mode"}
      </button>
    </div>
  );
};

export default Navbar;
