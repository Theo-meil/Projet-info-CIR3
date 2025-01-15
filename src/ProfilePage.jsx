import React from "react";
import {Link} from "react-router-dom";
import "./LoginPage.css"

function ProfilePage() {

    // Exemple de données utilisateur (à récup avec le backend)
    const userInfo = {
        name: "Nom",
        firstName: "Prénom",
        username: "NomUtilisateur",
        email: "utilisateur@example.com",
    };

    // Exemple de données d'événements (à récup dynamiquement)
    const userEvents = [
        { id: 1, name: "Tournoi FIFA 2025", date: "20 janvier 2025", qrCode: "monQrCode1" },
        { id: 2, name: "Championnat Call of Duty", date: "25 janvier 2025", qrCode: "monQrCode2" },
        { id: 3, name: "Compétition Fortnite", date: "30 janvier 2025", qrCode: "monQrCode3" },
    ];

    return (
        <div className="profile-container">
            <h1 className="profile-title">Profil de l'utilisateur</h1>

            {/* Section des informations de l'utilisateur */}
            <section className="user-info-section">
                <h2>Informations personnelles</h2>
                <p><strong>Nom :</strong> {userInfo.name}</p>
                <p><strong>Prénom :</strong> {userInfo.firstName}</p>
                <p><strong>Nom d'utilisateur :</strong> {userInfo.username}</p>
                <p><strong>Email :</strong> {userInfo.email}</p>
            </section>

            {/* Section des événements de l'utilisateur */}
            <section className="user-events-section">
                <h2>Événements payés</h2>
                {userEvents.length > 0 ? (
                    <table className="user-events-table">
                        <thead>
                        <tr>
                            <th>Nom</th>
                            <th>Date</th>
                            <th>QR Code</th>
                        </tr>
                        </thead>
                        <tbody>
                        {userEvents.map((event) => (
                            <tr key={event.id}>
                                <td>{event.name}</td>
                                <td>{event.date}</td>
                                <td>
                                    <img src={event.qrCode} alt={`QR Code for ${event.name}`} className="qr-code" />
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                ) : (
                    <p>Aucun événement payé pour le moment.</p>
                )}
            </section>

            {/* Bouton retour */}
            <Link to="/">
                <button className="back-button">Retour Menu</button>
            </Link>
        </div>
    );
}

export default ProfilePage;