import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'bdyoutube',
)

cursor = conexao.cursor() 

#CREATE
comando = 'INSERT INTO vendas (nome_produto, valor) VALUES ("lápis", 5)'
cursor.execute(comando)
conexao.commit()

#READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
comando = 'UPDATE vendas SET valor = 10 WHERE nome_produto = "caneta"'
cursor.execute(comando)
conexao.commit()

#DELETE
comando = 'DELETE FROM vendas WHERE nome_produto = "lápis"'
cursor.execute(comando)
conexao.commit()

cursor.close() 
conexao.close() 