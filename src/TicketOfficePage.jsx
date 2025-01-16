import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { Container, Typography, TextField, Button, Box, Alert } from "@mui/material";

function TicketOfficePage() {
    const location = useLocation();

    // Exemple de données de l'événement (à récup en backend)
    const event = location.state || {
        id: 1,
        name: "Tournoi FIFA",
        date: "20 janvier 2025",
        participants: 20,
        maxParticipants: 50,
        price: "20€",
    };

    const [formData, setFormData] = useState({
        firstName: "",
        lastName: "",
        email: "",
        cardNumber: "",
    });

    const [error, setError] = useState("");
    const [success, setSuccess] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Validation des données
        if (!formData.firstName || !formData.lastName || !formData.email || !formData.cardNumber) {
            setError("Tous les champs sont obligatoires.");
            setSuccess(false);
            return;
        }

        if (!/^\d{16}$/.test(formData.cardNumber)) {
            setError("Le numéro de carte doit contenir exactement 16 chiffres.");
            setSuccess(false);
            return;
        }

        setError("");
        setSuccess(true);

        // Simuler l'ajout de l'événement au profil
        console.log("Événement payé avec succès :", event.name, formData);
    };

    // Styles
    const containerStyle = {
        minHeight: "140vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#1a1a1a",
        color: "#fff",
    };

    const boxStyle = {
        backgroundColor: "#000",
        padding: "30px",
        borderRadius: "10px",
        maxWidth: "600px",
        width: "100%",
        boxShadow: "0 0 20px rgba(255, 255, 255, 0.2)",
        textAlign: "center",
    };

    const textFieldStyle = {
        marginBottom: "20px",
        backgroundColor: "#1a1a1a",
    };

    const labelPropsStyle = { color: "#fff" };
    const inputPropsStyle = { color: "#fff" };

    const buttonStyle = {
        backgroundColor: "#ff0000",
        color: "#fff",
        fontWeight: "bold",
    };

    const linkButtonStyle = {
        color: "#fff",
        borderColor: "#ffcc00",
    };

    return (
        <Container style={containerStyle}>
            <Box style={boxStyle}>
                {/* Informations sur l'événement */}
                <Typography variant="h4" style={{ marginBottom: "20px", color: "#ffcc00" }}>
                    {event.name}
                </Typography>
                <Typography variant="body1" style={{ marginBottom: "10px" }}>
                    Date : {event.date}
                </Typography>
                <Typography variant="body1" style={{ marginBottom: "10px" }}>
                    Participants : {event.participants} / {event.maxParticipants}
                </Typography>
                <Typography variant="body1" style={{ marginBottom: "20px", fontWeight: "bold" }}>
                    Prix : {event.price}
                </Typography>

                {/* Formulaire de paiement */}
                <form onSubmit={handleSubmit}>
                    <TextField
                        label="Prénom"
                        name="firstName"
                        variant="outlined"
                        fullWidth
                        value={formData.firstName}
                        onChange={handleChange}
                        style={textFieldStyle}
                        InputLabelProps={{ style: labelPropsStyle }}
                        inputProps={{ style: inputPropsStyle }}
                        required
                    />

                    <TextField
                        label="Nom"
                        name="lastName"
                        variant="outlined"
                        fullWidth
                        value={formData.lastName}
                        onChange={handleChange}
                        style={textFieldStyle}
                        InputLabelProps={{ style: labelPropsStyle }}
                        inputProps={{ style: inputPropsStyle }}
                        required
                    />

                    <TextField
                        label="Email"
                        name="email"
                        type="email"
                        variant="outlined"
                        fullWidth
                        value={formData.email}
                        onChange={handleChange}
                        style={textFieldStyle}
                        InputLabelProps={{ style: labelPropsStyle }}
                        inputProps={{ style: inputPropsStyle }}
                        required
                    />

                    <TextField
                        label="Numéro de carte bancaire"
                        name="cardNumber"
                        type="text"
                        variant="outlined"
                        fullWidth
                        value={formData.cardNumber}
                        onChange={handleChange}
                        style={textFieldStyle}
                        InputLabelProps={{ style: labelPropsStyle }}
                        inputProps={{ style: inputPropsStyle }}
                        required
                    />

                    {error && <Alert severity="error" style={{ marginBottom: "20px" }}>{error}</Alert>}
                    {success && <Alert severity="success" style={{ marginBottom: "20px" }}>Paiement réussi ! Retrouver la réservation dans votre profile  !</Alert>}

                    <Button
                        type="submit"
                        variant="contained"
                        fullWidth
                        style={buttonStyle}
                    >
                        Payer ma place
                    </Button>
                </form>

                <Link to="/" style={{ textDecoration: "none", marginTop: "20px", display: "block" }}>
                    <Button variant="outlined" fullWidth style={linkButtonStyle}>
                        Retour Menu
                    </Button>
                </Link>
            </Box>
        </Container>
    );
}

export default TicketOfficePage;
