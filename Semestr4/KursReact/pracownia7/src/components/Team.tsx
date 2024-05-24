import React, { useState } from "react";
import "../output.css";

type TeamMember = {
    id: number,
    name: string,
    position: string,
    bio: string,
    image: string
}

interface TeamProps {
    companyTeamMembers: TeamMember[]
}

const Team = (props: TeamProps) => {
    const { companyTeamMembers } = props;

    return (
        <section id="team" className="py-5">
            <div className="max-w-[800px] m-auto">
                <h2 className="text-[2.5em] mb-5 inline-block">Meet Our Team</h2>
                <div className="flex flex-wrap justify-center">
                    {companyTeamMembers.map((member) => (
                        <div key={member.id} className="flex-[0_0_calc(40%-40px)] p-5 m-2.5 text-center bg-light-team-member dark:bg-dark-team-member ">
                            <img src={member.image} alt={member.name} className="rounded-full x2mb-5" />
                            <div>
                                <h3 className="mb-2.5 inline-block">{member.name}</h3>
                                <p>{member.position}</p>
                                <p>{member.bio}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>

    );
}

export default Team;