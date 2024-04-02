/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';
import { darken, lighten } from 'polished';
import { colors } from './colors';

export const darkThemeStyles = css`
.dark-theme{
  background-color: ${colors.darkBackground};
  color: ${colors.darkText};

  .navbar {
    background-color: ${colors.navbarDarkBackground};
    a {
      color: ${colors.darkText};
    }
  }

  .theme-toggle-button {
    background-color: ${lighten(0.6, colors.darkBackground)};
    color: ${colors.lightText};
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: ${lighten(0.55, colors.darkBackground)};
    }
  }

  .content-card {
    background-color: ${colors.contentCardDarkBackground};
  }

  .team-member {
    background-color: ${darken(0.1, colors.darkBackground)};
    color: ${colors.darkText};
  }

  .blog-post {
    background-color: ${darken(0.2, colors.darkBackground)};
    color: ${colors.darkText};

    button {
      background-color: ${colors.buttonDarkBackground};
      color: ${colors.darkText};

      &:hover {
        background-color: ${colors.buttonHoverDarkBackground};
      }
    }
  }

  .section:nth-child(even) {
    background-color: ${darken(0.1, colors.darkBackground)};
  }

  .contact-form {
    background-color: ${darken(0.15, colors.darkBackground)};
    color: ${colors.darkText};
    border: 1px solid ${darken(0.25, colors.darkBackground)};
  }

  .contact {
    input[type="text"],
    input[type="email"],
    textarea {
      background-color: ${darken(0.15, colors.darkBackground)};
      color: ${colors.darkText};
      border: 1px solid ${darken(0.25, colors.darkBackground)};
    }

    button {
      background-color: ${colors.buttonDarkBackground};
      color: ${colors.darkText};

      &:hover {
        background-color: ${colors.buttonHoverDarkBackground};
      }
    }
  }
}
`;
