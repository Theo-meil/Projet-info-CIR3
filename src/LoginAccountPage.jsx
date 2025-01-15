import React from "react";
import { Link } from "react-router-dom";
import { Button, Container, Typography, TextField, Box } from "@mui/material";

function LoginAccountPage() {
    return (
        <Container style={{ minHeight: "100vh", display: "flex", justifyContent: "center", alignItems: "center", backgroundColor: "#1a1a1a" }}>
            <Box
                style={{
                    backgroundColor: "#000",
                    color: "#fff",
                    padding: "40px 30px",
                    borderRadius: "10px",
                    boxShadow: "0px 0px 20px rgba(255, 255, 255, 0.2)",
                    maxWidth: "400px",
                    width: "100%",
                    textAlign: "center",
                }}
            >
                <Typography variant="h4" style={{ marginBottom: "20px", color: "#ffcc00", fontFamily: '"Press Start 2P", cursive' }}>
                    Connexion
                </Typography>

                <TextField
                    label="Adresse Email"
                    variant="outlined"
                    fullWidth
                    style={{ marginBottom: "20px", backgroundColor: "#1a1a1a", borderColor: "#fff" }}
                    InputLabelProps={{ style: { color: "#fff" } }}
                    inputProps={{ style: { color: "#fff" } }}
                />

                <TextField
                    label="Mot de passe"
                    type="password"
                    variant="outlined"
                    fullWidth
                    style={{ marginBottom: "30px", backgroundColor: "#1a1a1a" }}
                    InputLabelProps={{ style: { color: "#fff" } }}
                    inputProps={{ style: { color: "#fff" } }}
                />

                <Button
                    variant="contained"
                    fullWidth
                    style={{ backgroundColor: "#ff0000", color: "#fff", marginBottom: "20px", fontWeight: "bold" }}
                >
                    Se connecter
                </Button>

                <Link to="/" style={{ textDecoration: "none" }}>
                    <Button variant="outlined" fullWidth style={{ color: "#fff", borderColor: "#ffcc00" }}>
                        Retour Menu
                    </Button>
                </Link>

                <Typography variant="body2" style={{ marginTop: "20px", color: "#ffffffb3" }}>
                    Pas encore de compte ? <Link to="/sign-up" style={{ color: "#ffcc00" }}>Inscrivez-vous</Link>
                </Typography>
            </Box>
        </Container>
    );
}

export default LoginAccountPage;
