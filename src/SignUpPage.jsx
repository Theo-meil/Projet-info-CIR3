import "./LoginPage.css"
import React, {useState} from "react";
import {Link} from "react-router-dom";
import HomePage from "./HomePage.jsx";

function SignUpPage() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
    });
    const [error, setError] = useState("");

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (formData.password !== formData.confirmPassword) {
            setError("Les mots de passe ne correspondent pas.");
            return;
        }
        setError("");
        console.log("Compte créé avec succès :", formData);
    };

    return (
        <div className="create-account-container">
            <h1>Créer un compte</h1>
            <form onSubmit={handleSubmit} className="create-account-form">
                <div className="form-group">
                    <label htmlFor="username">Nom d'utilisateur</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        variant="outlined"
                        fullWidth
                        value={formData.username}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    <TextField
                        label="Adresse Email"
                        name="email"
                        type="email"
                        variant="outlined"
                        fullWidth
                        value={formData.email}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    <TextField
                        label="Mot de passe"
                        name="password"
                        type="password"
                        variant="outlined"
                        fullWidth
                        value={formData.password}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    <TextField
                        label="Confirmer le mot de passe"
                        name="confirmPassword"
                        type="password"
                        variant="outlined"
                        fullWidth
                        value={formData.confirmPassword}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />
                </div>
                {error && <p className="error-message">{error}</p>}
                <button type="submit" className="submit-button">Créer mon compte</button>
                <Link to="/">
                    <button>Retour Menu</button>
                </Link>
            </form>
        </div>
    );
}

export default SignUpPage;
