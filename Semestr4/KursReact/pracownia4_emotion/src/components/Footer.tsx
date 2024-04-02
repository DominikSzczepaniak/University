import React from "react";
import { css } from "@emotion/react";

interface FooterProps {
  name: string;
}

const Footer: React.FC<FooterProps> = (props) => {
  const { name } = props;

  return (
    <footer
      css={css`
        padding: 20px 0;
        text-align: center;
      `}
    >
      <div>
        <p>
          &copy; {new Date().getFullYear()} {name}
        </p>
      </div>
    </footer>
  );
};

export default Footer;
