import os #importa a biblioteca para manipulação do S.O.
import mysql.connector #Importa o conector mySQL para o python

def conectarBD (host, usuario, senha, DB):
    connection=mysql.connector.connect( #Informando dados de conexão
        host = "localhost", #ip do servidor do banco de dados
        user = "root", #usuário cadastrado no MySQL
        password = "330165", #Senha do usuário cadastrado no MySQL
        database = "basepj" #Nome do database utilizado
    )
    return connection

def insertBD(marca, valor, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "INSERT INTO ativos (marca, valor) VALUES( %s, %s)"
    data = (
        marca,
        valor
    )
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações na tabela

    ativos_id = cursor.lastrowid #Obter o último ID cadastrado
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão
    print("Foi cadastrado o novo ativo!: ", ativos_id)
    
def insertBD2(nome, salario, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "INSERT INTO funcionarios (nome, salario) VALUES( %s, %s)"
    data = (
        nome,
        salario
    )
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações na tabela

    funcionario_id = cursor.lastrowid #Obter o último ID cadastrado
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão
    print("Foi cadastrado o novo funcionario!: ", funcionario_id)

def insertBD3(id_setor, id_funcionario, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "INSERT INTO ondetrabalha (id_setor, id_funcionario) VALUES(%s, %s)"
    data = (
        id_setor,
        id_funcionario
    )
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações na tabela

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão
    print("Foi cadastrada a regiao de serviço!")

def insertBD4(id_setor, id_ativo, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "INSERT INTO qualsetor (id_setor, id_ativo) VALUES(%s, %s)"
    data = (
        id_setor,
        id_ativo
    )
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações na tabela

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão
    print("Foi cadastrada a regiao de serviço onde esta o ativo!")


def read_BD(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM ativos"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT

def read_BD2(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM funcionarios"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT

def read_BD3(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT f.nome, s.nome, f.salario FROM setores s, funcionarios f, ondetrabalha ot WHERE ot.id_setor = s.id AND ot.id_funcionario = f.id"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT

def read_BD4(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT a.marca, s.nome, a.valor FROM setores s, ativos a, qualsetor ql WHERE ql.id_setor = s.id AND ql.id_ativo = a.id"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT

def updateBD(id, marca, valor, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE ativos SET  marca=%s, valor=%s WHERE ID=%s"
    data = (
        id,
        marca,
        valor,
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados")

def updateBD2(id, nome, salario, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE funcionarios SET  nome=%s, salario=%s WHERE ID=%s"
    data = (
        id,
        nome,
        salario,
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados")

def updateBD3(id_setor, id_funcionario, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE ondetrabalha SET id_setor=%s WHERE id_funcionario=%s"
    data = (
        id_setor,
        id_funcionario,
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados")

def updateBD4(id_setor, id_ativo, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE qualsetor SET id_setor=%s WHERE id_ativo=%s"
    data = (
        id_setor,
        id_ativo,
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados")


def deleteBD(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM ativos WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")
   
def deleteBD2(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM funcionarios WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")

def deleteBD3(id_funcionario, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM ondetrabalha WHERE id_funcionario = %s"
    data = (id_funcionario, )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")

def deleteBD4(id_ativo, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM qualsetor WHERE id_ativo = %s"
    data = (id_ativo, )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")

import time
while(True):
    print("\n\n:::::: GERENCIADOR DE CADASTRO DE ATIVOS E FUNCIONARIOS ::::::")
    print("1 - Cadastrar Ativo")
    print("2 - Exibir ativos cadastrados")
    print("3 - Atualizar dados do ativo")
    print("4 - Deletar cadastro do ativo")
    print("5 - Cadastrar funcionário")
    print("6 - Exibir funcionários cadastrados")
    print("7 - Atualizar dados do funcionário")
    print("8 - Deletar cadastro do funcionário")
    print("9 - Registrar o setor onde o funcionário trabalha, sendo 1 RH, 2 Financeiro, 3 Desenvolvedor, 4 Suporte, 5 Comercial, 6 Produção")
    print("10 - Mostrar onde os funcionários trabalham")
    print("11 - Alterar o setor de trabalho do funcionario")
    print("12 - Deletar o registro do funcionário")
    print("13 - Registrar o setor onde o ativo esta, sendo 1 RH, 2 Financeiro, 3 Desenvolvedor, 4 Suporte, 5 Comercial, 6 Produção")
    print("14 - Mostrar em qual setor os ativos se encontram")
    print("15 - Alterar o setor do ativo")
    print("16 - Deletar o registro do ativo")
    print("17 - Sair")

    opcao = input("Digite a opção desejada:")

    if(opcao == "1"):
        marca = input("Digite a marca do ativo: ")
        valor = input("Digite o valor do ativo: ")
        connection = conectarBD("localhost","root", "admin", "projeto")
        insertBD(marca, valor, connection)
    time.sleep(3)

    if(opcao == "2"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        read_BD(connection)
        time.sleep(3)

    if(opcao == "3"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id = input("Informe o ID do ativo:")
        marca = input("Informe a marca atualizada:")
        valor = input("Informe o novo valor:")
        updateBD(marca, valor, id, connection)
    time.sleep(3)

    if (opcao == "4"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id = input("Informe o ID do ativo:")
        deleteBD(id, connection)
        time.sleep(3)

    if(opcao == "5"):
        nome = input("Digite o nome do funcionario: ")
        salario = input("Digite o salario do funcionario: ")
        connection = conectarBD("localhost","root", "admin", "projeto")
        insertBD2(nome, salario, connection)

    if(opcao == "6"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        read_BD2(connection)
        time.sleep(3)
    
    if(opcao == "7"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id = input("Informe o ID do funcionario:")
        nome = input("Informe o novo nome do funcionario:")
        salario = input("Informe o novo salario do funcionario:")
        updateBD2(nome, salario, id, connection)

    if (opcao == "8"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id = input("Informe o ID do funcionario:")
        deleteBD2(id, connection)
        time.sleep(3)

    if(opcao == "9"):
        id_setor = input("Digite o id do setor onde ele(a) trabalha: ")
        id_funcionario = input("Digite o id do funcionario: ")
        connection = conectarBD("localhost","root", "admin", "projeto")
        insertBD3(id_setor, id_funcionario, connection)

    if(opcao == "10"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        read_BD3(connection)
        time.sleep(3)

    if(opcao == "11"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id_funcionario = input("Informe o id do funcionario que quer alterar de setor:")
        id_setor = input("Informe o novo setor do funcionario:")
        updateBD3(id_setor, id_funcionario, connection)

    if (opcao == "12"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id_funcionario = input("Informe o ID do funcionario que quer deletar do registro:")
        deleteBD3(id_funcionario, connection)
        time.sleep(3)

    if(opcao == "13"):
        id_setor = input("Digite o id do setor onde o ativo esta: ")
        id_ativo = input("Digite o id do ativo: ")
        connection = conectarBD("localhost","root", "admin", "projeto")
        insertBD4(id_setor, id_ativo, connection)

    if(opcao == "14"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        read_BD4(connection)
        time.sleep(3)

    if(opcao == "15"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id_ativo = input("Informe o id do ativo que quer alterar de setor:")
        id_setor = input("Informe o novo setor do ativo:")
        updateBD4(id_setor, id_ativo, connection)

    if (opcao == "16"):
        connection = conectarBD("localhost","root", "admin", "projeto")
        id_ativo= input("Informe o ID do ativo que quer deletar do registro:")
        deleteBD4(id_ativo, connection)
        time.sleep(3)

    if(opcao == "17"):
        break
