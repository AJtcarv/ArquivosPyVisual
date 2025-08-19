import pyodbc 

dados_conexao = (
    "Driver={SQL Server};" 
    "Server=Arleson-Dell;"
    "Database=PythonSQL;"
)


conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()
id = int(input('id: '))
cliente = str(input("Cliente: "))
produto = str(input('Produto: '))
data = str(input('data: (formato yyyy-mm-dd)'))
preco = int(input('Preço: '))
quantidade = int(input('Quantidade: '))

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade) 
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()