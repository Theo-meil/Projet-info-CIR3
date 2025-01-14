import React from "react";
import {Link} from "react-router-dom";

function ProfilePage() {
    return (
        <div>
        <p>Profile page</p>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default ProfilePage;