import './HomePage.css';
import React from "react";
import { Link } from 'react-router-dom';

function HomePage() {

    const tournaments = [
        {id: 1, name: "FIFA", date: "14 janvier 2025", prize: "1000€"},
        {id: 2, name: "CoD", date: "2025-15-01", prize: "1500€"},
        {id: 3, name: "Lol", date: "2025-16-01", prize: "2000€"},
    ];

    return (
        <div className="homepage-container">

            <header className="top-bar">
                <div className="user-info">Bienvenue, NomUtilisateur</div>
                <div className="auth-buttons">
                    <Link to="/login-account">
                        <button className="login-button">Login</button>
                    </Link>
                    <Link to="/sign-up-account">
                        <button className="sign-up-button">Sign up</button>
                    </Link>
                    <Link to="/profile">
                        <button className="profile-button">Profile</button>
                    </Link>
                    <button className="disonnect-button">Disconnect</button>
                </div>
            </header>


            <div className="hero-section">
                <h1 className="hero-title">Bienvenue aux tournois de jeux vidéo</h1>
                <p className="hero-subtitle">Rejoignez des compétitions épiques et montrez vos talents !</p>
                <Link to="/create-event">
                    <button className="event-button">Créer un event</button>
                </Link>
                <Link to="/join-event">
                    <button className="event-button">Rejoindre un event</button>
                </Link>
            </div>

            <section className="tournaments-section">
                <h2 className="section-title">Tournois disponibles</h2>
                <ul className="tournaments-list">
                    {tournaments.map((tournament) => (
                        <li key={tournament.id} className="tournament-item">
                            <h3 className="tournament-name">{tournament.name}</h3>
                            <p className="tournament-date">Date : {tournament.date}</p>
                            <p className="tournament-prize">Récompense : {tournament.prize}</p>
                            <button className="details-button">Voir détails</button>
                        </li>
                    ))}
                </ul>
            </section>

            <footer className="footer">
                <p>&copy; 2025 Tournois de Jeux Vidéo. Tous droits réservés.</p>
                <nav className="footer-nav">
                    <a href="#">Contact</a>
                    <a href="#">Conditions d'utilisation</a>
                    <a href="#">Politique de confidentialité</a>
                </nav>
            </footer>
        </div>
    );
}

export default HomePage;