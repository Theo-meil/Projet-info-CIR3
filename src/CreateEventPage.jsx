import React from "react";
import {Link} from "react-router-dom";

function CreateEventPage() {
    return (
        <div>
            <p>Create Event page</p>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default CreateEventPage;