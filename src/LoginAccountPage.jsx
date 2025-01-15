import React, {useState} from "react";
import {Link} from "react-router-dom";
import "./LoginPage.css"

function LoginAccountPage() {

    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!formData.email || !formData.password) {
            setError("Veuillez remplir tous les champs.");
            return;
        }
        setError('');
        // Logique pour envoyer les données à une API ou un backend
        console.log("Connexion réussie :", formData);
    };

    return (
        <div className="login-container">
            <h1 className="login-title">Connexion</h1>
            <form onSubmit={handleSubmit} className="login-form">
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Mot de passe</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div>
                {error && <p className="error-message">{error}</p>}

                <button type="submit" className="submit-button">Se connecter</button>

                <Link to="/">
                    <button type="button" className="signup-link">Retour menu</button>
                </Link>
            </form>
        </div>
    );
}

export default LoginAccountPage;