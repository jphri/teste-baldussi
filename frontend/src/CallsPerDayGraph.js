import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

export default function CallsTimeSeries() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/calls/calls_per_day", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`, // se tiver auth
      },
    })
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  return (
    <div style={{ width: "100%", height: 400 }}>
      <h2>Total de Chamadas por Dia</h2>
      <ResponsiveContainer>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="data" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="total" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}