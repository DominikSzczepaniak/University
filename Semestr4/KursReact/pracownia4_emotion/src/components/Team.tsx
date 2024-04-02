import TeamCard from "./TeamCard";
import { css } from "@emotion/react";

interface TeamProps {
  teamMembers: {
    id: number;
    name: string;
    position: string;
    bio: string;
    image: string;
  }[];
}

const Team: React.FC<TeamProps> = (props) => {
  const { teamMembers } = props;

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
          Meet Our Team
        </h2>
        <div
          css={css`
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
          `}
        >
          {teamMembers.map((member) => (
            <TeamCard
              key={member.id}
              id={member.id}
              name={member.name}
              position={member.position}
              bio={member.bio}
              image={member.image}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Team;
