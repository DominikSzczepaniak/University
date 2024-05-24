import React, { ReactNode } from 'react';
import { Link } from "react-router-dom";

interface LayoutProps {
  children?: ReactNode; 
}

const Layout = ({ children }: LayoutProps) => {
    return (
        <div>
          <nav className="bg-white shadow-md sticky top-0 z-50 px-4 py-2">
            <ul className="flex justify-center space-x-4">
              <li><Link to="/" className="text-blue-500 hover:text-blue-700">Home</Link></li>
              <li><Link to="/about" className="text-blue-500 hover:text-blue-700">About Me</Link></li>
              <li><Link to="/projects" className="text-blue-500 hover:text-blue-700">Projects</Link></li>
            </ul>
          </nav>
          <main className="pt-4">
            {children}
          </main>
        </div>
      );
};

export default Layout;
