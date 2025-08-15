import { useEffect, useState } from 'react';

function CallsList() {
  const [calls, setCalls] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/calls/get')
      .then(res => res.json())
      .then(data => setCalls(data.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Lista de Chamadas</h2>
	  <table>
	  	<thead>
	  	<tr>
		  <th>ID Empresa</th>
		  <th>ID Chamada</th>
		  <th>Data</th>
		  <th>Cliente Nome</th>
		  <th>Origem</th>
		  <th>Campanha</th>
		  <th>Operador</th>
		  <th>Destino</th>
		  <th>Recurso</th>
		  <th>Recursos</th>
		  <th>Recurso Detalhado</th>
		  <th>Centro de Custo</th>
		  <th>Duracao Real</th>
		  <th>Duracao</th>
		  <th>Preço</th>
		  <th>SIP Code</th>
		  <th>AMD</th>
		  <th>Protocolo de Atendimento</th>
		  <th>Motivo de desligamento</th>
		  <th>Link Gravacao</th>
		  <th>Nome Ultima Fala</th>
		  <th>Tempo de Espera Ultima Fila</th>
		  <th>Tempo de Operador Ultima Fila</th>
		  <th>Tempo de espera total filas</th>
		  <th>Tempo de operador total filas</th>
	  	</tr>
	  	</thead>
	  	<tbody>
        {
			calls.map((data, idx) => (
				<tr key={idx}>
					<td>{data.empresa_id}</td>
					<td>{data.chamada_id}</td>
					<td>{data.data}</td>
					<td>{data.cliente_nome}</td>
					<td>{data.origem}</td>
					<td>{data.campanha}</td>
					<td>{data.operador}</td>
					<td>{data.destino}</td>
					<td>{data.recurso}</td>
					<td>{data.recursos}</td>
					<td>{data.recursos_detalhado}</td>
					<td>{data.centro_de_custo}</td>
					<td>{data.duracao_real}</td>
					<td>{data.duracao}</td>
					<td>{data.preco}</td>
					<td>{data.sip_code}</td>
					<td>{data.amd}</td>
					<td>{data.protocolo_atendimento}</td>
					<td>{data.motivo_desligamento}</td>
					<td>{data.link_gravacao}</td>
					<td>{data.nome_ultima_fila}</td>
					<td>{data.tempo_espera_ultima_fila}</td>
					<td>{data.tempo_operador_ultima_fila}</td>
					<td>{data.tempo_espera_total_filas}</td>
					<td>{data.tempo_operador_total_filas}</td>
				</tr>
			))
		}
	  	</tbody>
	  </table>
    </div>
  );
}

export default CallsList;
