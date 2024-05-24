/** @jsxImportSource @emotion/react */
import { ThemeProvider, css } from "@emotion/react";
import NavbarHeader from "./components/Navbar";
import About from "./components/About";
import Services from "./components/Services";
import Team from "./components/Team";
import Blog from "./components/Blog";
import ContactForm from "./components/ContactForm";
import Footer from "./components/Footer";
import { useState } from "react";
import { lightThemeStyles } from "./css/LightTheme";
import { darkThemeStyles } from "./css/DarkTheme";
import Navbar from "./components/Navbar";
import Header from "./components/Header";
import { darken, lighten } from "polished";

const companyData = {
  name: "Acme Corporation",
  slogan: "Innovation at its best",
  about:
    "We are a leading provider of innovative solutions in various industries. Our team is dedicated to delivering high-quality products and services to our clients worldwide.",
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
      description:
        "Designing intuitive user interfaces for optimal user experience.",
    },
    {
      id: 4,
      name: "Digital Marketing",
      description:
        "Promoting products and services through various online channels.",
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
      content:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
    },
    {
      id: 2,
      title: "Design Trends for 2024",
      date: "February 28, 2024",
      content:
        "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
    },
    {
      id: 3,
      title: "The Power of Social Media",
      date: "February 15, 2024",
      content:
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
    },
    {
      id: 4,
      title: "Artificial Intelligence in Business",
      date: "January 30, 2024",
      content:
        "Suspendisse eget sapien vitae eros tincidunt ultrices. Morbi nec sem nisi. Nulla ultrices odio et eros varius, a eleifend velit tristique.",
    },
    {
      id: 5,
      title: "The Impact of Virtual Reality",
      date: "January 15, 2024",
      content:
        "Integer auctor neque mauris, eget sagittis justo tristique sit amet. Nam at nibh et nulla suscipit blandit eu nec mi.",
    },
  ],
};

const colors = {
    lightBackground: "#fff",
    darkBackground: "#111",
    lightText: "#333",
    darkText: "#fff",
    navbarLightBackground: "#f0f0f0",
    navbarDarkBackground: "#222",
    contentCardLightBackground: "#eee",
    contentCardDarkBackground: "#333",
    buttonLightBackground: "#333",
    buttonDarkBackground: "#ddd",
    buttonLightText: "#fff",
    buttonDarkText: "#333",
    buttonHoverLightBackground: "#555",
    buttonHoverDarkBackground: "#ccc"
};



const lightTheme = {
    background: colors.lightBackground,
    text: colors.lightText,
    navbarBackground: colors.navbarLightBackground,
    buttonBackground: colors.buttonLightBackground,
    contentCardBackground: colors.contentCardLightBackground,
    buttonText: colors.buttonLightText,
    buttonHoverBackground: colors.buttonHoverLightBackground
}

const darkTheme = {
    background: colors.darkBackground,
    text: colors.darkText,
    navbarBackground: colors.navbarDarkBackground,
    buttonBackground: colors.buttonDarkBackground,
    contentCardBackground: colors.contentCardDarkBackground,
    buttonText: colors.buttonDarkText,
    buttonHoverBackground: colors.buttonHoverDarkBackground
}

const App = () => {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <ThemeProvider theme={darkMode ? darkTheme : lightTheme}>
    <div
      css={css`
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        color: ${darkMode ? colors.darkText : colors.lightText};
        background-color: ${darkMode ? darken(0.1, colors.darkBackground) : lighten(0.02, colors.lightBackground)};
        
      `}
    >
      <div
        css={css`
          margin: 0 auto;
          background-color: ${darkMode ? colors.contentCardDarkBackground : colors.contentCardLightBackground};
        `}
      >
        <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />
        <Header name={companyData.name} slogan={companyData.slogan} />
        <div
          css={css`
            border-radius: 10px;
            margin: 20px 0;

          
            & > :nth-child(odd) {
              background-color: ${darkMode ? darken(0.1, colors.contentCardDarkBackground) : lighten(0.5,  colors.contentCardLightBackground)};
            }
          `}
        >
          <About about={companyData.about} />
          <Services services={companyData.services} />
          <Team teamMembers={companyData.teamMembers} />
          <Blog blogPosts={companyData.blogPosts} />
          <ContactForm />
        </div>
        <Footer name={companyData.name} />
      </div>
    </div>
    </ThemeProvider>    
  );
};

export default App;
