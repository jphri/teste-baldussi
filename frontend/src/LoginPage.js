import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const res = await fetch("http://localhost:8000/auth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded", // importante!
        },
        body: new URLSearchParams({
          username,
          password,
        }),
      });

      if (!res.ok) {
        throw new Error("Usuário ou senha inválidos");
      }

      const data = await res.json();
      localStorage.setItem("token", data.access_token);

      navigate("/kpi");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <form
        onSubmit={handleLogin}
      >
        <h1>Login</h1>

        {error && <p>{error}</p>}

        <div>
          <label>Usuário</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div>
          <label>Senha</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button
          type="submit"
        >
          Entrar
        </button>
      </form>
    </div>
  );
}