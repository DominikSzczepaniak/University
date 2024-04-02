import React from "react";
import { css } from "@emotion/react";

interface HeaderProps {
  name: string;
  slogan: string;
}

const NavbarHeader: React.FC<HeaderProps> = (props) => {
  const { name, slogan } = props;
  return (
    <header
      css={css`
        padding: 50px 0;
        text-align: center;
      `}
    >
      <div>
        <h1
          css={css`
            font-size: 3em;
            margin-bottom: 10px;
          `}
        >
          {name}
        </h1>
        <p
          css={css`
            font-size: 1.5em;
          `}
        >
          {slogan}
        </p>
      </div>
    </header>
  );
};

export default NavbarHeader;
