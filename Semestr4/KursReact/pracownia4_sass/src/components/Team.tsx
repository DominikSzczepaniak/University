import "../styles.css";
import TeamCard from "./TeamCard";

interface teamProps {
    teamMembers: {
        id: number;
        name: string;
        position: string;
        bio: string;
        image: string;
    }[];

}

function Team(props: teamProps) {
    const companyData = props;
    return (
        <section id="team" className="section team">
            <div className="section-content">
                <h2>Meet Our Team</h2>
                <div className="team-members">
                    {companyData.teamMembers.map((member) => (
                        <TeamCard id={member.id} name={member.name} position={member.position} bio={member.bio} image={member.image}/>
                    ))}
                </div>
            </div>
        </section>
    )
}

export default Team;