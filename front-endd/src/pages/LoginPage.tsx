import { useState } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/api/users/login", {
  username_or_email: email,
  password,
});

      const token = res.data.access_token;

      login(token);
      navigate("/dashboard"); // Redirige tras login exitoso
    } catch (err) {
      setErrorMsg("Correo o contraseña inválidos ❌");
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-bold mb-4">Iniciar sesión</h2>

        {errorMsg && (
          <p className="text-red-600 text-sm mb-3">{errorMsg}</p>
        )}

        <div className="mb-4">
          <label className="block mb-1 text-sm font-medium">Email</label>
          <input
            type="email"
            className="w-full px-3 py-2 border rounded-md"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <label className="block mb-1 text-sm font-medium">Contraseña</label>
          <input
            type="password"
            className="w-full px-3 py-2 border rounded-md"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button
          type="submit"
          className="bg-indigo-600 text-white w-full py-2 rounded-md hover:bg-indigo-700 transition"
        >
          Entrar
        </button>
        <p className="mt-3 text-sm text-center">
  ¿No tienes cuenta?{" "}
  <a href="/register" className="text-blue-600 hover:underline">
    Regístrate aquí
  </a>
</p>
      </form>
    </div>
  );
}