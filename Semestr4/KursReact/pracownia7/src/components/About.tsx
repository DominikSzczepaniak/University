import React, { useState } from "react";
import "../output.css";

interface AboutProps{
    companyAbout: string
}

const About = (props: AboutProps) => {
    const { companyAbout } = props;
    return (
        <section id="about" className="py-5">
        <div className="max-w-[800px] m-auto">
            <h2 className="text-[2.5em] mb-5 inline-block">About Us</h2>
            <p>{companyAbout}</p>
        </div>
        </section>
    )
}

export default About;