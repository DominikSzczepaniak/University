import React, { useState } from "react";
import "../output.css";

interface HeaderProps {
    companyName: string,
    companySlogan: string
}

const Header = (props: HeaderProps) => {
    const { companyName, companySlogan } = props;
    return (
        <div id="header" className="py-[50px] text-center">
            <h1 className="text-6xl mb-2.5">{companyName}</h1>
            <p className="text-3xl">{companySlogan}</p>
        </div>
    )
}

export default Header;