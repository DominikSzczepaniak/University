/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';

export const navbarHeaderStyles = css`
  .navbar {
    position: sticky;
    top: 0;
    padding: 10px 0;
    text-align: center;
    z-index: 1000;

    a {
      text-decoration: none;
      padding: 0 20px;
    }
  }

  .header {
    padding: 50px 0;
    text-align: center;

    h1 {
      font-size: 3em;
      margin-bottom: 10px;
    }

    p {
      font-size: 1.5em;
    }
  }

  .theme-toggle-button {
    cursor: pointer;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
  }
`;
