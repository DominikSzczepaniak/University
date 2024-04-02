/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';
import { darken, lighten } from 'polished';
import { colors } from './colors';

export const lightThemeStyles = css`
.light-theme{
  background-color: ${colors.lightBackground};
  color: ${colors.lightText};

  .navbar {
    background-color: ${colors.navbarLightBackground};
    a {
      color: ${colors.lightText};
    }
  }

  .theme-toggle-button {
    background-color: ${colors.lightText};
    color: ${colors.darkBackground};
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: ${darken(0.2, colors.lightText)};
    }
  }

  .content-card {
    background-color: ${colors.contentCardLightBackground};
  }

  .team-member {
    background-color: ${lighten(0.02, colors.lightBackground)};
    color: ${colors.lightText};
  }

  .blog-post {
    background-color: ${lighten(0.05, colors.contentCardLightBackground)};
    color: ${colors.lightText};

    button {
      background-color: ${colors.buttonLightBackground};
      color: ${colors.darkBackground};

      &:hover {
        background-color: ${colors.buttonHoverLightBackground};
      }
    }
  }

  .section:nth-child(even) {
    background-color: ${lighten(0.02, colors.lightBackground)};
  }

  .contact-form {
    background-color: ${lighten(0.04, colors.lightBackground)};
    color: ${colors.lightText};
    border: 1px solid ${darken(0.1, colors.lightBackground)};
  }

  .contact {
    input[type="text"],
    input[type="email"],
    textarea {
      background-color: ${colors.lightBackground};
      color: ${colors.lightText};
      border: 1px solid ${darken(0.1, colors.lightBackground)};
    }

    button {
      background-color: ${colors.buttonLightBackground};
      color: ${colors.darkBackground};

      &:hover {
        background-color: ${colors.buttonHoverLightBackground};
      }
    }
  }
}
`;
