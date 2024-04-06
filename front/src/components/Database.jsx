import React from "react";

import './database.css';
import aged from '../images/aged.jpg';
import animal from '../images/animal.jpg';
import community from '../images/community.jpg';
import emergency from '../images/emergency.jpg';
import picture5 from '../images/picture5.webp';
import hospital from '../images/hospital.jpg';


function Database() {
    return (
        <div>
            <h1>find a charity</h1>
            <a href="https://crewcode2024-dzmyt2hprnwrjjshdarvte.streamlit.app/">
                <div id="charities">

                    <Organisation image={aged} text="Aged care" />
                    <Organisation image={animal} text="Animal protection" />
                    <Organisation image={community} text="Economic social and community development" />
                    <Organisation image={emergency} text="Emergency relief" />
                    <Organisation image={picture5} text="Environmental activities" />
                    <Organisation image={hospital} text="Hospital services and rehabilitation activities" />

                </div>
            </a>

        </div>
    )
}

function Organisation({ image, text }) {
    return (
        <div className="organisation">
            <img src={image} alt={text} />
            <p>{text}</p>
        </div>
    );
}


export default Database