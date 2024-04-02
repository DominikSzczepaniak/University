interface ServicesProps {
    services: {
        id: number;
        name: string;
        description: string;
    }[];
}

const Services: React.FC<ServicesProps> = (props) => {
    const { services } = props;

    return (
        <section id="services" className="section services">
            <div className="section-content">
                <h2>Our Services</h2>
                <ul>
                    {services.map((service) => (
                        <li key={service.id}>
                            <h3>{service.name}</h3>
                            <p>{service.description}</p>
                        </li>
                    ))}
                </ul>
            </div>
        </section>
    );
};

export default Services;
