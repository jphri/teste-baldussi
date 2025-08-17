import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function CallsTable() {
  const [calls, setCalls] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
      return;
    }

    async function fetchCalls() {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:8000/calls/get?page=${page}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const data = await res.json();
        setCalls(data.data || []); // supondo que o backend retorna { items: [...], total: N }
      } catch (err) {
        console.error("Erro ao buscar chamadas:", err);
      }
      setLoading(false);
    }
    fetchCalls();
  }, [page]);

  return (
    <div>
      <h2>Lista de Chamadas</h2>
      {loading ? (
        <p>Carregando...</p>
      ) : (
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              <th>Empresa</th>
              <th>Chamada ID</th>
              <th>Data</th>
              <th>Origem</th>
              <th>Destino</th>
              <th>Duração</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {calls.length === 0 ? (
              <tr>
                <td colSpan="7">Nenhuma chamada encontrada</td>
              </tr>
            ) : (
              calls.map((call) => (
                <tr key={call.chamada_id}>
                  <td>{call.empresa_id}</td>
                  <td>{call.chamada_id}</td>
                  <td>{call.data}</td>
                  <td>{call.origem}</td>
                  <td>{call.destino}</td>
                  <td>{call.duracao_real}</td>
                  <td>{call.motivo_desligamento}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      )}

      <div style={{ marginTop: "10px" }}>
        <button onClick={() => setPage((p) => Math.max(1, p - 1))}>Anterior</button>
        <span style={{ margin: "0 10px" }}>Página {page}</span>
        <button onClick={() => setPage((p) => p + 1)}>Próxima</button>
      </div>
    </div>
  );
}
