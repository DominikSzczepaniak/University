import classes from "./Footer.module.scss";
import { ReactNode } from 'react';

export default function Footer({ content }: { content: ReactNode }) {
    return (
        <footer className={classes["footer"]}>
            <div className={classes["footer-content"]}>
                <p>{content}</p>
            </div>
        </footer>
    );
}
