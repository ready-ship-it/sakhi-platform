import { useNavigate } from "react-router-dom";

export default function Login() {
  const nav = useNavigate();

  return (
    <div>
      <h2>Admin Login</h2>
      <button onClick={() => nav("/dashboard")}>Login</button>
    </div>
  );
}
