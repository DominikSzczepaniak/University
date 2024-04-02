import { css, useTheme } from "@emotion/react";

interface TeamCardProps {
  id: number;
  name: string;
  position: string;
  bio: string;
  image: string;
}

const TeamCard: React.FC<TeamCardProps> = (props) => {
  const { id, name, position, bio, image } = props;
  const theme = useTheme();
  return (
    <div
      key={id}
      css={css`
        flex: 0 0 calc(33.33% - 20px);
        padding: 20px;
        margin: 10px;
        text-align: center;
        background-color: ${theme.background};
        color: ${theme.text};
      `}
    >
      <img
        src={image}
        alt={name}
        css={css`
          border-radius: 50%;
          margin-bottom: 20px;
        `}
      />
      <div>
        <h3
          css={css`
            margin-bottom: 10px;
            display: inline-block;
          `}
        >
          {name}
        </h3>
        <p>{position}</p>
        <p>{bio}</p>
      </div>
    </div>
  );
};

export default TeamCard;
