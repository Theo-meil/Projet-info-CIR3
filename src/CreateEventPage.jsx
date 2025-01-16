import React, { useState } from "react";
import {Link} from "react-router-dom";

export function CreateEventPage() {
    const [eventData, setEventData] = useState({
        eventName: "",
        eventCreator: "",
        participationFee: "",
        prize: "",
        maxParticipants: "",
        description: "",
        eventDate: "", // Ajout du champ pour la date
        eventImage: null,
    });
    const [eventCode, setEventCode] = useState(null);
    const [showPaymentMessage, setShowPaymentMessage] = useState(false);

    // Fonction pour générer un code d'événement unique
    const generateEventCode = () => {
        const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        let code = "#";
        for (let i = 0; i < 8; i++) {
            code += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return code;
    };

    // Fonction pour gérer les changements dans le formulaire
    const handleChange = (e) => {
        const { name, value } = e.target;
        setEventData((prev) => ({ ...prev, [name]: value }));
    };

    // Gestion de l'image insérée par l'utilisateur
    const handleImageUpload = (e) => {
        const file = e.target.files[0];
        if (file) {
            setEventData((prev) => ({ ...prev, eventImage: URL.createObjectURL(file) }));
        }
    };

    // Fonction pour soumettre le formulaire
    const handleSubmit = () => {
        if (
            !eventData.eventName ||
            !eventData.eventCreator ||
            !eventData.participationFee ||
            !eventData.prize ||
            !eventData.maxParticipants ||
            !eventData.eventDate // Vérification de la date
        ) {
            alert("Veuillez remplir tous les champs !");
            return;
        }

        // Simule le paiement
        setShowPaymentMessage(true);

        setTimeout(() => {
            // Génère un code d'événement après le paiement
            const newEventCode = generateEventCode();
            setEventCode(newEventCode);
            setShowPaymentMessage(false);
            alert(`Événement créé avec succès ! Code d'événement : ${newEventCode}`);
        }, 2000); // Délai simulé pour le paiement
    };

    return (
        <div style={styles.page}>
            <Menu />
            <h1 style={styles.title}>Créez un évènement</h1>
            <div style={styles.form}>
                <label style={styles.label}>Organisateur</label>
                <input
                    type="text"
                    name="eventCreator"
                    value={eventData.eventCreator}
                    onChange={handleChange}
                    style={styles.input}
                    placeholder="Nom de l'organisateur..."
                />
                <label style={styles.label}>Nom de l'évènement</label>
                <input
                    type="text"
                    name="eventName"
                    value={eventData.eventName}
                    onChange={handleChange}
                    style={styles.input}
                    placeholder="Nom de l'évènement..."
                />

                <label style={styles.label}>Ajoutez une image</label>
                <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageUpload}
                    style={styles.fileInput}
                />
                {eventData.eventImage && (
                    <div style={styles.imagePreview}>
                        <img
                            src={eventData.eventImage}
                            alt="Aperçu"
                            style={styles.image}
                        />
                    </div>
                )}

                <label style={styles.label}>Date de l'évènement</label>
                <input
                    type="date"
                    name="eventDate"
                    value={eventData.eventDate}
                    onChange={handleChange}
                    style={styles.input}
                />

                <label style={styles.label}>Tarif de Participation (€)</label>
                <input
                    type="number"
                    name="participationFee"
                    value={eventData.participationFee}
                    onChange={handleChange}
                    style={styles.input}
                    placeholder="Tarif"
                />

                <label style={styles.label}>Prix à Gagner (€)</label>
                <input
                    type="number"
                    name="prize"
                    value={eventData.prize}
                    onChange={handleChange}
                    style={styles.input}
                    placeholder="Prix pour le gagnant"
                />

                <label style={styles.label}>Nombre de Participants</label>
                <input
                    type="number"
                    name="maxParticipants"
                    value={eventData.maxParticipants}
                    onChange={handleChange}
                    style={styles.input}
                    placeholder="Nombre de participants..."
                />

                <label style={styles.label}>Description</label>
                <textarea
                    name="description"
                    value={eventData.description}
                    onChange={handleChange}
                    style={styles.textarea}
                    placeholder="Ajoutez une description (facultatif)"
                />

                <button onClick={handleSubmit} style={styles.submitButton}>
                    Créer l'Événement
                </button>
            </div>

            {eventCode && (
                <div style={styles.eventCode}>
                    <h2>Votre événement a été créé avec succès !</h2>
                    <p>
                        <strong>Code d'Événement :</strong> {eventCode}
                    </p>
                </div>
            )}
        </div>
    );
}

// Menu en haut de la page
function Menu() {
    return (
        <div style={styles.menu}>
            <Link to="/">
                <button style={styles.menuButton}>Retour</button>
            </Link>
        </div>
    );
}

// Styles pour le composant
const styles = {
    page: {
        minHeight: "100vh",
        minWidth: "130vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#1a1a1a",
        color: "#fff",
        padding: "20px",
    },
    title: {
        fontSize: "36px",
        fontWeight: "bold",
        marginBottom: "20px",
        color: "#ffcc00",
        textAlign: "center",
    },
    form: {
        backgroundColor: "#000",
        padding: "30px",
        borderRadius: "10px",
        maxWidth: "600px",
        width: "100%",
        boxShadow: "0 0 20px rgba(255, 255, 255, 0.2)",
        display: "flex",
        flexDirection: "column",
        gap: "20px",
    },
    label: {
        fontWeight: "bold",
        marginBottom: "5px",
        color: "#fff",
    },
    input: {
        width: "100%",
        padding: "10px",
        border: "1px solid #444",
        borderRadius: "5px",
        backgroundColor: "#1a1a1a",
        color: "#fff",
        fontSize: "16px",
    },
    textarea: {
        width: "100%",
        height: "100px",
        padding: "10px",
        border: "1px solid #444",
        borderRadius: "5px",
        backgroundColor: "#1a1a1a",
        color: "#fff",
        fontSize: "16px",
    },
    fileInput: {
        padding: "10px",
        borderRadius: "5px",
        backgroundColor: "#1a1a1a",
        color: "#fff",
    },
    imagePreview: {
        marginTop: "10px",
        textAlign: "center",
    },
    image: {
        maxWidth: "100%",
        maxHeight: "200px",
        borderRadius: "10px",
    },
    submitButton: {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        padding: "10px 15px",
        cursor: "pointer",
        fontSize: "16px",
        fontWeight: "bold",
        textTransform: "uppercase",
        width: "100%",
    },
    menu: {
        width: "100%",
        marginBottom: "20px",
        display: "flex",
        justifyContent: "center",
    },
    menuButton: {
        backgroundColor: "#ffcc00",
        color: "#000",
        border: "none",
        borderRadius: "5px",
        padding: "10px 15px",
        cursor: "pointer",
        fontSize: "16px",
        fontWeight: "bold",
        fontFamily: '"Orbitron", sans-serif',
    },
    eventCode: {
        marginTop: "30px",
        backgroundColor: "#000",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0 0 20px rgba(255, 255, 255, 0.2)",
        textAlign: "center",
        color: "#ffcc00",
    },
};


export default CreateEventPage;