import React, { useState } from "react";
import {Link} from "react-router-dom";

export function JoinEventPage() {
    const [add, setAdd] = useState(''); // Champ d'ajout de participant

    // Fonction pour ajouter un participant
    const handleBarreEvent = () => {
        if (add.trim() === '') {
            alert("Veuillez entrer un code d'évènement");
            return;
        }
        alert("Ça fonctionne");
        setAdd(''); // Réinitialiser le champ de recherche
    };

    return (
        <div style={styles.page}>
            <Menu />
            <h1 style={styles.myHead}>
                Entrez le code de l'évènement
            </h1>
            <div>
                {/* Barre de recherche pour ajouter un participant */}
                <Barre
                    add={add}
                    onBarreChange={setAdd}
                    onBarreEvent={handleBarreEvent}
                />
            </div>
        </div>
    );
}

// Composant d'ajout de participant (incluant la barre de recherche)
function Barre({ add, onBarreChange, onBarreEvent }) {
    return (
        <div style={styles.addContainer}>
            <input
                type="text"
                style={styles.input}
                value={add}
                placeholder="Code d'évènement..."
                onChange={(e) => onBarreChange(e.target.value)} // Gère le changement de texte
            />
            <Link to="/show-event">
                <button style={styles.addButton} onClick={onBarreEvent}>Rejoindre</button>
            </Link>
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

// Styles
const styles = {
    page: {
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
        marginBottom: "10px",
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
    addButton: {
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

    myHead: {
        fontSize: "36px",
        fontWeight: "bold",
        marginBottom: "20px",
        color: "#ffcc00",
        textAlign: "center",
    }

};


export default JoinEventPage