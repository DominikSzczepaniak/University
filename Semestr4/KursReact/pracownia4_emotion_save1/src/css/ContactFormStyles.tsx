import { css } from '@emotion/react';

export const contactFormStyles = css`
  .contact {
    margin-bottom: 40px;

    .form-group {
      margin-bottom: 20px;
    }

    input[type="text"],
    input[type="email"],
    textarea {
      width: calc(100% - 20px);
      padding: 10px;
      border-radius: 5px;
      border: none;
      margin-top: 5px;
    }

    textarea {
      resize: vertical;
    }

    button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
  }

  .contact-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
  }
`;