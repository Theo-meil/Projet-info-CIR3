import React from "react";
import {Link} from "react-router-dom";

function LoginAccountPage() {
    return (
        <div>
            <p>Login Account page</p>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default LoginAccountPage;