import { css, useTheme } from "@emotion/react";

function ContactForm() {
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };
  const theme = useTheme();

  return (
    <section
      id="contact"
      css={css`
        max-width: 800px;
        margin: 0 auto;
        margin-bottom: 40px;
        background-color: ${theme.background};
        color: ${theme.text};
        border: 1px solid ${theme.background};

      `}
    >
      <div className="section-content">
        <h2>Contact Us</h2>
        <form
          onSubmit={handleSubmit}
          css={css`
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            background-color: ${theme.background};
            color: ${theme.text};
            border: 1px solid ${theme.background};
          `}
        >
          <div
            css={css`
              margin-bottom: 20px;
            `}
          >
            <input
              type="text"
              placeholder="Name"
              required
              css={css`
                width: calc(100% - 20px);
                padding: 10px;
                border-radius: 5px;
                border: none;
                margin-top: 5px;

        background-color: ${theme.background};
        color: ${theme.text};
        border: 1px solid ${theme.background};
              `}
            />
          </div>
          <div
            css={css`
              margin-bottom: 20px;
            `}
          >
            <input
              type="email"
              placeholder="Email"
              required
              css={css`
                width: calc(100% - 20px);
                padding: 10px;
                border-radius: 5px;
                border: none;
                margin-top: 5px;

        background-color: ${theme.background};
        color: ${theme.text};
        border: 1px solid ${theme.background};
              `}
            />
          </div>
          <div
            css={css`
              margin-bottom: 20px;
            `}
          >
            <textarea
              rows={5}
              placeholder="Message"
              required
              css={css`
                width: calc(100% - 20px);
                padding: 10px;
                border-radius: 5px;
                border: none;
                margin-top: 5px;
                resize: vertical;

        background-color: ${theme.background};
        color: ${theme.text};
        border: 1px solid ${theme.background};
              `}
            ></textarea>
          </div>
          <button
            type="submit"
            css={css`
              padding: 10px 20px;
              border: none;
              border-radius: 5px;
              cursor: pointer;
              transition: background-color 0.3s ease;
              background-color: ${theme.buttonBackground};
              color: ${theme.buttonText};
              &:hover {
                background-color: ${theme.buttonHoverBackground};
              }
            `}
          >
            Send Message
          </button>
        </form>
      </div>
    </section>
  );
}

export default ContactForm;
