// Navbar.js
import React from 'react';
import { Link } from "react-scroll";
import '../index.css'

function Navbar() {
    return (
        <header>
            <div className='navbar'>
                <a className="name" href="/">Flach</a>
                <Link to="about">About us</Link>
                <Link to="charities">Find a charity</Link>
                <Link to="faqs">FAQs</Link>
                <Link to="contact">Contact us</Link>
            </div>
        </header>
    );
}

export default Navbar;
