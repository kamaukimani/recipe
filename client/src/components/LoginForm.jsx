import React, { useState } from "react";
import { Button, Error, Input, FormField, Label } from "../styles";

function LoginForm({ onLogin, API_URL }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    fetch(`${API_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials:"include" ,
      body: JSON.stringify({ username, password }),
    }).then((r) => {
      setIsLoading(false);
      if (r.ok) {
        r.json().then((user) => onLogin(user));
      } else{
        r.json().then(data=>{
          setError(data.message)
        })
      }
    })
    .catch(err=> {
      setError(err.message + "... "+ "Check your connection to the Server")
      setIsLoading(false)
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <FormField>
        <Label htmlFor="username">Username</Label>
        <Input
          type="text"
          id="username"
          autoComplete="off"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </FormField>
      <FormField>
        <Label htmlFor="password">Password</Label>
        <Input
          type="password"
          id="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </FormField>
      <FormField>
        <Button variant="fill" color="primary" type="submit">
          {isLoading ? "Loading..." : "Login"}
        </Button>
      </FormField>
      <FormField>
        {/* {errors.map((err) => (
          <Error key={err}>{err}</Error>
        ))} */}
        {error && <p style={{color:"red"}}>{error}</p>}
      </FormField>
    </form>
  );
}

export default LoginForm;