import { useEffect, useState } from "react";
import API from "../api/api";

export default function Insights() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/admin/insights").then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h1>Insights</h1>
      {data.map((d, i) => (
        <p key={i}>{d.category} - {d.sentiment}</p>
      ))}
    </div>
  );
}
