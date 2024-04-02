interface FooterProps {
    name: string;
}

const Footer: React.FC<FooterProps> = (props) => {
    const { name } = props;

    return (
        <footer className="footer">
            <div className="footer-content">
                <p>&copy; {new Date().getFullYear()} {name}</p>
            </div>
        </footer>
    );
};

export default Footer;
