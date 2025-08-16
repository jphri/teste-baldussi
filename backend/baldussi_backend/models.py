from sqlalchemy import Column, Integer, String, String, Boolean, DateTime, Float
from baldussi_backend.database import Base

# Modelo de tabela
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)

class Call(Base):
    __tablename__ = "calls"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(String, index=True)
    chamada_id = Column(String, unique=True, index=True)
    data = Column(DateTime)
    cliente_nome = Column(String)
    origem = Column(String)
    campanha = Column(String, nullable=True)
    operador = Column(String, nullable=True)
    destino = Column(String)
    recurso = Column(String, nullable=True)
    recursos = Column(String, nullable=True)
    recursos_detalhado = Column(String, nullable=True)
    centro_de_custo = Column(String, nullable=True)
    duracao_real = Column(Integer, nullable=True)
    duracao = Column(Integer, nullable=True)
    preco = Column(String, nullable=True)
    sip_code = Column(String, nullable=True)
    amd = Column(String, nullable=True)
    protocolo_atendimento = Column(String, nullable=True)
    motivo_desligamento = Column(String, nullable=True)
    link_gravacao = Column(String, nullable=True)
    nome_ultima_fila = Column(String, nullable=True)
    tempo_espera_ultima_fila = Column(Integer, nullable=True)
    tempo_operador_ultima_fila = Column(Integer, nullable=True)
    tempo_espera_total_filas = Column(Integer, nullable=True)
    tempo_operador_total_filas = Column(Integer, nullable=True)
