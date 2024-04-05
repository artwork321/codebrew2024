import React from "react";

function About() {
    return (
        <div className="second_sec">
            <div id="about">
                <h1 className="title">about us</h1>
                <p className="homepage_text"> Welcome to Flach, where philanthropy meets simplicity. We're a dedicated team
                    of developers
                    who recognised the need for a user-friendly platform to connect
                    donors with reputable charities.
                </p>

                <div className="mission_box">
                    <p className="mission_text"><strong>Our mission is simple</strong></p>
                    <div className="box">
                        <p>To make charitable giving easy, transparent, and impactful.</p>
                    </div>
                </div>

                <p className="homepage_text">
                    Driven by the belief that everyone should have access to effective ways to support causes they care
                    about, we've crafted a search engine that streamlines the process of finding and supporting vetted
                    charitable organisations.
                </p>

                <p className="homepage_text">
                    With just a few clicks, users can explore a diverse array of causes, learn about impactful
                    initiatives, and contribute to positive change.
                </p>
            </div>
        </div>
    )
}

export default About;