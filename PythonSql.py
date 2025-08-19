import pyodbc 

dados_conexao = (
    "Driver={SQL Server};" 
    "Server=Arleson-Dell;"
    "Database=PythonSQL;"
)


conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()
id = "6"
cliente = "joana"
produto = "carro"
data = "2025/12/25"
preco = "9000"
quantidade = "1"

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade) 
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()