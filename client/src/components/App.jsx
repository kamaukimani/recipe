import React, { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "../pages/Login";
import RecipeList from "../pages/RecipeList";
import NewRecipe from "../pages/NewRecipe";

function App() {

    const API_URL="http://localhost:5555"
    const [user, setUser] = useState(null);

    useEffect(() => {
        // auto-login
        fetch(`${API_URL}/check_session`,{
            credentials:"include" ,
        }).then((r) => {
        if (r.ok) {
            r.json().then((user) => setUser(user));
        }
        });
    }, []);

    if (!user) return <Login onLogin={setUser} API_URL={API_URL}/>;

    return (
        <>
        {user ? <h1>Welcome {user.username}!</h1> : null}
        <NavBar user={user} setUser={setUser} API_URL={API_URL}/>
        <main>
            <Routes>
                <Route 
                    path="/new"
                    element={<NewRecipe user={user} API_URL={API_URL}/>}
                />
                <Route 
                    path="/"
                    element={<RecipeList API_URL={API_URL}/>}
                />
            </Routes>
        </main>
        </>
    );
}

export default App;