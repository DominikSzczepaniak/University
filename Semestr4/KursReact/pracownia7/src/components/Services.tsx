import React, { useState } from "react";
import "../output.css";

type Service = {
    id: number,
    name: string,
    description: string
}

interface ServicesProps {
    companyServices: Service[]
}

const Services = (props: ServicesProps) => {
    const { companyServices } = props;
    return (
        <section id="services" className="py-5">
            <div className="max-w-[800px] m-auto">
                <h2 className="text-[50px] mb-5 inline-block">Our Services</h2>
                <ul className="list-none p-0 m-0">
                    {companyServices.map((service) => (
                        <li className="p-0 m-0 list-none" key={service.id}>
                            <h3 className="text-[30px] mb-2.5">{service.name}</h3>
                            <p>{service.description}</p>
                        </li>
                    ))}
                </ul>
            </div>
        </section>
    );
}

export default Services;