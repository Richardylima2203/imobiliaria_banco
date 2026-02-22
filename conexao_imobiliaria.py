import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="segundo_banco"

)
print("✅ Conexão estabelecida com sucesso!\n")

cursor = conexao.cursor()

cursor.close()
conexao.close()
print("\n🔒 Conexão encerrada com sucesso!")
