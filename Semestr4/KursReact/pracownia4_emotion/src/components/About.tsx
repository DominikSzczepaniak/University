import { css } from "@emotion/react";

interface aboutProps {
  about: string;
}

function About(props: aboutProps) {
  const companyData = props;

  return (
    <section
      css={css`
        padding: 20px 0;
      `}
    >
      <div
        css={css`
          max-width: 800px;
          margin: 0 auto;
        `}
      >
        <h2
          css={css`
            font-size: 2.5em;
            margin-bottom: 20px;
            display: inline-block;
          `}
        >
          About Us
        </h2>
        <p>{companyData.about}</p>
      </div>
    </section>
  );
}

export default About;
