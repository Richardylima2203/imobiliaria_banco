
# Conexao com o banco de dados e consulta na tabela clientes com limite de 30 usuarios.

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="segundo_banco"

)
print("✅ Conexão estabelecida com sucesso!\n")

cursor = conexao.cursor()

cursor.execute("Select * from clientes order by nome limit 30")


print("📋 Clientes abaixo:\n")
for (clientes) in cursor.fetchall():
    print(clientes)

cursor.close()
conexao.close()
print("\n🔒 Conexão encerrada com sucesso!")


# CONEXAO COM O BANCO DE DADOS E EXECUTANDO CONSULTAS COM JOIN,WHERE E AS


conexao = mysql.connector.connect(
    host="nome_do_servidor",
    user="usuario",
    password="senha",
    database="nome_do_banco"
)
print("✅ Conexão estabelecida com sucesso!\n")


cursor = conexao.cursor()


consulta = """
SELECT
    c.id_cliente AS ID,
    c.nome AS Nome,
    c.email AS Email,
    x.cidade AS Cidade,
    x.estado AS Estado
FROM clientes AS c
INNER JOIN cep AS x
ON c.cep = x.cep
WHERE x.estado = 'SP'
ORDER BY c.nome;
"""
cursor.execute(consulta)


print("📍 Clientes de São Paulo:\n")
for (id_cliente, nome, email, cidade, estado) in cursor.fetchall():
    print(
        f"ID: {id_cliente:<3} | Nome: {nome:<25} | Email: {email:<30} | {cidade} - {estado}")

cursor.close()
conexao.close()
print("\n🔒 Conexão encerrada com sucesso!")
