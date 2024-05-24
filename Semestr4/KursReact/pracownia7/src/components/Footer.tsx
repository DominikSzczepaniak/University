import React, { useState } from "react";
import "../output.css";

interface FooterProps{
    companyName: string
}

const Footer = (props: FooterProps) => {
    const { companyName } = props;
    return (
        <footer className="py-5 text-center">
        <div>
          <p>
            &copy; {new Date().getFullYear()} {companyName}
          </p>
        </div>
      </footer>
    )
}

export default Footer;