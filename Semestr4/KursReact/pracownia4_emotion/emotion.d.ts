import '@emotion/react';

declare module '@emotion/react' {
  export interface Theme {
    background: string;
    text: string;
    navbarBackground: string;
    buttonBackground: string;
    contentCardBackground: string;
    buttonText: string;
    buttonHoverBackground: string;
  }
}