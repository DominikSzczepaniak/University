import React, { createContext, useState, useContext, ReactNode, FC } from 'react';

type Theme = 'light' | 'dark';

interface ITheme {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ITheme | undefined>(undefined);

export const useTheme = (): ITheme => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

interface ThemeProviderProps {
  children: ReactNode;
}

export const ThemeProvider: FC<ThemeProviderProps> = ({ children }) => {
  const [theme, setTheme] = useState<Theme>('light');

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
