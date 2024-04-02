import "../styles.css"

interface TeamCardProps {
    id: number;
    name: string;
    position: string;
    bio: string;
    image: string;
}

function TeamCard(props: TeamCardProps) {
    const member = props;
    return (
        <div key={member.id} className="team-member">
            <img src={member.image} alt={member.name} />
            <div>
                <h3>{member.name}</h3>
                <p>{member.position}</p>
                <p>{member.bio}</p>
            </div>
        </div>
    )
}

export default TeamCard;