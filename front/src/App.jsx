// App.js
import React from 'react';
import './index.css'; // Import your CSS file
import Navbar from './components/Navbar.jsx';
import Content from './components/Content.jsx';
import Footer from './components/Footer.jsx';
import About from './components/About.jsx';
import Faqs from './components/Faqs.jsx';
import Database from './components/Database.jsx'

function App() {
    return (
        <div>
            <Navbar />
            <Content />
            <Database />
            <About />
            <Faqs />
            <Footer />
        </div>
    );
}

export default App;
