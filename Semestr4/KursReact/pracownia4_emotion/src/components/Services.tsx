import { css } from "@emotion/react";

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
          Our Services
        </h2>
        <ul
          css={css`
            list-style: none;
            padding: 0;
            margin: 0;
          `}
        >
          {services.map((service) => (
            <li
              css={css`
                margin-bottom: 20px;
                text-align: left;
              `}
              key={service.id}
            >
              <h3
                css={css`
                  font-size: 1.8em;
                  margin-bottom: 10px;
                `}
              >
                {service.name}
              </h3>
              <p>{service.description}</p>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
};

export default Services;
