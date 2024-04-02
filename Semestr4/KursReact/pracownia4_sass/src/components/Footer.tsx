import "../styles.css";

interface footerProps {
    name: string;
}


function Footer(props: footerProps) {
    const companyData = props;
    return (
        <footer className="footer">
            <div className="footer-content">
                <p>
                    &copy; {new Date().getFullYear()} {companyData.name}
                </p>
            </div>
        </footer>
    )
}

export default Footer;