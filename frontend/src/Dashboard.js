import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import CallsTable from "./CallsTable";

export default function Dashboard() {
  const [kpis, setKpis] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
      return;
    }

    const fetchKPIs = async () => {
      try {
        const res = await fetch("http://localhost:8000/calls/kpi", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!res.ok) {
          if (res.status === 401) {
            // token inválido ou expirado → volta para login
            localStorage.removeItem("token");
            navigate("/login");
          }
          throw new Error("Erro ao buscar KPIs");
        }

        const data = await res.json();
        setKpis(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchKPIs();
  }, [navigate]);

  if (error) return <p>Erro: {error}</p>;
  if (!kpis) return <p>Carregando...</p>;

  return (
    <div>
      <h1>Dashboard</h1>
      <p><strong>Total de Chamadas:</strong> {kpis.total}</p>
      <p><strong>Atendidas:</strong> {kpis.atendidas}</p>
      <p><strong>ASR:</strong> {kpis.asr}%</p>
      <p><strong>ACD (tempo médio):</strong> {kpis.acd} segundos</p>
      <CallsTable/>
    </div>
  );
}