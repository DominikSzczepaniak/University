import React, { useState } from "react";
import "../output.css";

interface NavbarProps{
    darkMode: boolean;
    toggleTheme: () => void;
}

const Navbar = (props: NavbarProps) => {
    const { darkMode, toggleTheme } = props;
    return (
        <div className="sticky top-0 py-2.5 text-center z-1000 bg-light-navbar-bg dark:bg-dark-navbar-bg">
            <a href="#header" className="px-4 no-underline text-light-text dark:text-dark-text">Home</a>
            <a href="#about" className="px-4 no-underline text-light-text dark:text-dark-text">About</a>
            <a href="#services" className="px-4 no-underline text-light-text dark:text-dark-text">Services</a>
            <a href="#team" className="px-4 no-underline text-light-text dark:text-dark-text">Team</a>
            <a href="#blog" className="px-4 no-underline text-light-text dark:text-dark-text">Blog</a>
            <a href="#contact" className="px-4 no-underline text-light-text dark:text-dark-text">Contact</a>
            <button onClick={toggleTheme} className="cursor-pointer py-2.5 px-5 transition duration-300 ease-in-out rounded-md bg-light-toggle-button-bg dark:bg-dark-toggle-button-bg hover:bg-light-hover hover:dark:bg-dark-hover text-light-bg dark:text-dark-content-card">
            {darkMode ? "Light Mode" : "Dark Mode"}
            </button>
        </div>
    );
}

export default Navbar;