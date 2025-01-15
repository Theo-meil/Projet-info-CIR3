import "./LoginPage.css"
import React, {useState} from "react";
import {Link} from "react-router-dom";

function SignUpPage() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
    });

    const [error, setError] = useState('');

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData({...formData, [name]: value});
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (formData.password !== formData.confirmPassword) {
            setError('Les mots de passe ne correspondent pas.');
            return;
        }
        setError('');
        // Logique pour envoyer les données à une API ou un backend
        console.log('Compte créé avec succès :', formData);
    };

    return (
        <div className="create-account-container">
            <h1 className="sign-up-title">Créer un compte</h1>
            <form onSubmit={handleSubmit} className="create-account-form">
                <div className="form-group">
                    <label htmlFor="username">Nom d'utilisateur</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                </div>
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
                <div className="form-group">
                    <label htmlFor="confirmPassword">Confirmer le mot de passe</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        name="confirmPassword"
                        value={formData.confirmPassword}
                        onChange={handleChange}
                        required
                    />
                </div>
                {error && <p className="error-message">{error}</p>}
                <button type="submit" className="submit-button">Créer mon compte</button>
                <Link to="/">
                    <button type="button" >Retour Menu</button>
                </Link>
            </form>
        </div>
    );
}

export default SignUpPage