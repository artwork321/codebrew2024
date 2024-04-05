// Navbar.js
import React from 'react';
import { Link } from "react-router-dom";

function Navbar() {
    return (
        <div className="navbar">
            <a className="name" href="/">Flach</a>
            <a href="/#about">About us</a>
            <Link to="/database">Find a charity</Link>
            <a href="/#faqs">FAQs</a>
            <a href="/#contact">Contact us</a>
        </div>
    );
}

export default Navbar;
