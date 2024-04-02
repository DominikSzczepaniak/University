/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';
import NavbarHeader from './components/NavbarHeader';
import About from './components/About';
import Services from './components/Services';
import Team from './components/Team';
import Blog from './components/Blog';
import ContactForm from './components/ContactForm';
import Footer from './components/Footer';
import { useState } from 'react';
import { lightThemeStyles } from './css/LightTheme';
import { darkThemeStyles } from './css/DarkTheme';
import { blogPostStyles, blogPostsStyles } from './css/BlogStyles';
import { contactFormStyles } from './css/ContactFormStyles';
import { footerStyles } from './css/FooterStyles';
import { navbarHeaderStyles } from './css/NavbarHeaderStyles';
import { servicesStyles } from './css/ServicesStyles';
import { teamMemberStyles, teamMembersStyles } from './css/TeamStyles';

const bodyStyle = css`
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
`;

const portfolioStyle = css`
.portfolio{
  margin: 0 auto;
}
`;

const contentCardStyle = css`
.content-card{
    border-radius: 10px;
    margin: 20px 0;
}
`;


const sectionStyle = css`
.section{
    padding: 20px 0;

    h2 {
        font-size: 2.5em;
        margin-bottom: 20px;
        display: inline-block;
    }
}
`;

const sectionContentStyle = css`
.section-content{
    max-width: 800px;
    margin: 0 auto;
}
`


const companyData = {
    name: "Acme Corporation",
    slogan: "Innovation at its best",
    about: "We are a leading provider of innovative solutions in various industries. Our team is dedicated to delivering high-quality products and services to our clients worldwide.",
    services: [
        {
            id: 1,
            name: "Web Development",
            description: "Creating modern and responsive websites.",
        },
        {
            id: 2,
            name: "Mobile App Development",
            description: "Building mobile applications for iOS and Android.",
        },
        {
            id: 3,
            name: "UI/UX Design",
            description: "Designing intuitive user interfaces for optimal user experience.",
        },
        {
            id: 4,
            name: "Digital Marketing",
            description: "Promoting products and services through various online channels.",
        },
    ],
    teamMembers: [
        {
            id: 1,
            name: "Alice Young",
            position: "CEO",
            bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
            image: "https://via.placeholder.com/150",
        },
        {
            id: 2,
            name: "Jane Smith",
            position: "CTO",
            bio: "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
            image: "https://via.placeholder.com/150",
        },
        {
            id: 3,
            name: "Alice Johnson",
            position: "Lead Designer",
            bio: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
            image: "https://via.placeholder.com/150",
        },
    ],
    blogPosts: [
        {
            id: 1,
            title: "The Future of Technology",
            date: "March 10, 2024",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
        },
        {
            id: 2,
            title: "Design Trends for 2024",
            date: "February 28, 2024",
            content: "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
        },
        {
            id: 3,
            title: "The Power of Social Media",
            date: "February 15, 2024",
            content: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
        },
        {
            id: 4,
            title: "Artificial Intelligence in Business",
            date: "January 30, 2024",
            content: "Suspendisse eget sapien vitae eros tincidunt ultrices. Morbi nec sem nisi. Nulla ultrices odio et eros varius, a eleifend velit tristique.",
        },
        {
            id: 5,
            title: "The Impact of Virtual Reality",
            date: "January 15, 2024",
            content: "Integer auctor neque mauris, eget sagittis justo tristique sit amet. Nam at nibh et nulla suscipit blandit eu nec mi.",
        },
    ],
};

const App = () => {
    const [darkMode, setDarkMode] = useState(false);

    return (
        !darkMode ? 
        <div css={[bodyStyle, blogPostStyles, blogPostsStyles, contactFormStyles, footerStyles, servicesStyles, teamMemberStyles, teamMembersStyles, portfolioStyle, lightThemeStyles, contentCardStyle, sectionContentStyle, sectionStyle, navbarHeaderStyles]}>
            <div className={`portfolio ${darkMode ? "dark-theme" : "light-theme"}`}>
                <NavbarHeader darkMode={darkMode} setDarkMode={setDarkMode} name={companyData.name} slogan={companyData.slogan} />
                <div className="content-card" >
                    <About about={companyData.about} />
                    <Services services={companyData.services} />
                    <Team teamMembers={companyData.teamMembers} />
                    <Blog blogPosts={companyData.blogPosts} />
                    <ContactForm />
                </div>
                <Footer name={companyData.name} />
            </div>
        </div>
        :
        <div css={[bodyStyle, blogPostStyles, blogPostsStyles, contactFormStyles, footerStyles, servicesStyles, teamMemberStyles, teamMembersStyles, portfolioStyle, darkThemeStyles, contentCardStyle, sectionContentStyle, sectionStyle, navbarHeaderStyles]}>
            <div className={`portfolio ${darkMode ? "dark-theme" : "light-theme"}`}>
                <NavbarHeader darkMode={darkMode} setDarkMode={setDarkMode} name={companyData.name} slogan={companyData.slogan} />
                <div className="content-card">
                    <About about={companyData.about} />
                    <Services services={companyData.services} />
                    <Team teamMembers={companyData.teamMembers} />
                    <Blog blogPosts={companyData.blogPosts} />
                    <ContactForm />
                </div>
                <Footer name={companyData.name} />
            </div>
        </div>
    );
};

export default App;
