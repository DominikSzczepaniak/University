import TitleSubtitle from "./components/TitleSubtitle";
import Photo from "./components/Photo";
import ContactInfo from "./components/ContactInfo";
import { Skills } from "./components/Skill";
import "./styles.css";

export default function Card() {
  return (
    <div className="Card">
      <Photo />
      <TitleSubtitle
        title="Dominik Szczepaniak"
        subtitle="Software Engineer"
        titleFontSize={30}
        subtitleFontSize={25}
      />
      <TitleSubtitle title="Uwr" titleFontSize={20} />
      <ContactInfo
        phoneNumber="123-456-789"
        email="f9Ykz@example.com"
        github="dominikszczepaniak"
      />
      <TitleSubtitle
        title="About me"
        subtitle="cos cos cos cos cos cos cos cos cos cos cos cos cos 
        cos cos cos cos cos cos cos cos cos cos cos cos cos cos c
        os cos cos cos cos cos cos cos cos cos cos cos cos cos cos "
        titleFontSize={25}
        subtitleFontSize={20}
      />
      <TitleSubtitle title="Skills" titleFontSize={25} />
      <div className="skillsSection">
        <Skills title="React" />
        <Skills title="JavaScript" />
        <Skills title="Java" />
        <Skills title="Python" />
        <Skills title="Rust" />
        <Skills title="SQL" />
        <Skills title="PostgreSQL" />
      </div>
    </div>
  );
}
