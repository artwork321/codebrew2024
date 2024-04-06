// Main.js
import React from 'react';
import { Link } from "react-scroll";

function Content() {
    return (
        <div className="first_sec">
            <div className="introduction">
                <h1>Flach</h1>
                <h2>Connecting you to charities</h2>
                <Link to="charities">
                    <p className="button">find a charity</p>
                </Link>
            </div>
        </div>
    );
}

export default Content;
