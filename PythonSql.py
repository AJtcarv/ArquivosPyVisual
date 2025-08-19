import pyodbc 

dados_conexao = (
    "Driver={SQL Server};" 
    "Server=Arleson-Dell;"
    "Database=PythonSQL;"
)


conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade) 
VALUES
    (4, 'camille', 'geladeira', '2025/08/11', 4500, 1),
    (5, 'jorge', 'frigobar', '2025/08/15', 7000, 1)"""

cursor.execute(comando)
cursor.commit()