interface TeamCardProps {
  id: number;
  name: string;
  position: string;
  bio: string;
  image: string;
}

const TeamCard: React.FC<TeamCardProps> = (props) => {
  const { id, name, position, bio, image } = props;

  return (
    <div key={id} className="team-member">
      <img src={image} alt={name} />
      <div>
        <h3>{name}</h3>
        <p>{position}</p>
        <p>{bio}</p>
      </div>
    </div>
  );
};

export default TeamCard;
