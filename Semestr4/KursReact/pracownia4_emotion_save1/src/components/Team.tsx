import TeamCard from './TeamCard';

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
        <section id="team" className="section team">
            <div className="section-content">
                <h2>Meet Our Team</h2>
                <div className="team-members">
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
