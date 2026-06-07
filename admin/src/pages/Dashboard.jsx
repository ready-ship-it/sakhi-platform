import { useEffect, useState } from "react";
import API from "../api/api";

export default function Dashboard() {
  const [data, setData] = useState({});

  useEffect(() => {
    API.get("/admin/stats").then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Users: {data.users}</p>
      <p>Messages: {data.messages}</p>
    </div>
  );
}
