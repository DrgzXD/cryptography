"""
pedir para a pessoa digitar uma frase
cryptografar a frase
pedir 2 senhas ou o padrao
descryptografar 
pedir para a pessoa digitar as senhas ou o padrao
"""

lista_com_a_frase_criptografada = []
lista_com_a_frase_descpriptografada =  []

como_vai_ser_feita_a_criptografia = input("Como deseja ultilizar a criptografia: [P]adrão, [C]haveada ou [A]mbos: ") #Perguntando ao usuario qual vai ser o tipo de criptografia que ele deseja
aux = como_vai_ser_feita_a_criptografia.upper()
if aux == "P" and aux != "A" and aux != "C":                #Condicionando para qual o usuario desejar.
    var = int(input("Digite o valor padrao que deseja seguir: "))
elif aux == "C" and aux != "P" and aux != "A":              #Condicionando para qual o usuario desejar.
    id = input("Digite o id: ")
    password = input("Digite a senha: ")
    var = 7
elif aux == "A" and aux != "P" and aux != "C":              #Condicionando para qual o usuario desejar.
    var = int(input("Digite o valor padrao que deseja seguir: "))
    id = input("Digite uma chave: ")
    password = input("Digite uma senha: ")
else:
    print("Digite somente UM dos valores requeridos")       #Caso ele nao de nenhum dos valores verdadeiros, uma saida para o recomeco.
        
        
        
texto_a_ser_criptografado = input("Digite o que deseja criptografar: ")
tam = len(texto_a_ser_criptografado)

    
for i in range(0,tam):                  #Adicionando toda a frase que o usuario deseja criptografar a uma lista em forma decimal.
    texto_criptografado = ord(texto_a_ser_criptografado[i]) + var
    lista_com_a_frase_criptografada.append(texto_criptografado)  
    
print(lista_com_a_frase_criptografada)  #Mostrando para o usuario como ficou a frase criptografada

#Verificando se o usuario que vai receber e descriptografar o codigo sabe o padrao e(ou) a senha que foi chaveada.
verificaçao_de_como_foi_feita_a_criptografia = input("Como foi feita a criptografia: [P]adrão, [C]haveada ou [A]mbos: ") 
verificaçao_de_como_foi_feita_a_criptografia_up = verificaçao_de_como_foi_feita_a_criptografia.upper()
if verificaçao_de_como_foi_feita_a_criptografia_up == "C" and aux != "A" and aux != "P":
    verificacao_da_senha = input("Digite a senha: ")
    verificacao_do_id = input("Digite o id: ")
    while verificacao_da_senha != password:
        print("Senha incorreta")
        verificacao_da_senha = input("Tente novamente: ")
    while verificacao_do_id != id:
        print("Id incorreto")
        verificacao_do_id = input("Tente novamente: ")
    print("OK")
    tam_lista_criptografada = len(lista_com_a_frase_criptografada)
    for i in range(0,tam_lista_criptografada):
        texto_descriptografado = (lista_com_a_frase_criptografada[i]) - var
        frase_descriptografada = chr(texto_descriptografado)
        lista_com_a_frase_descpriptografada.append(frase_descriptografada)
        
    print(f"a frase criptografada foi {lista_com_a_frase_descpriptografada}")
        
    
    
elif verificaçao_de_como_foi_feita_a_criptografia_up == "P" and aux != "C" and aux != "A":
    var_padrao = int(input("Digite o valor padrao"))
    while var_padrao != var:
        print("Erro, valor errado, tente novamente")
        var_padrao = int(input("Digite o valor padrao: "))
    print("OK")
    tam_lista_criptografada = len(lista_com_a_frase_criptografada)
    for i in range(0,tam_lista_criptografada):
        texto_descriptografado = (lista_com_a_frase_criptografada[i]) - var
        frase_descriptografada = chr(texto_descriptografado)
        lista_com_a_frase_descpriptografada.append(frase_descriptografada)
        
    print(f"a frase criptografada foi {lista_com_a_frase_descpriptografada}")
    
    
    
elif verificaçao_de_como_foi_feita_a_criptografia_up == "A" and aux != "P" and aux != "C":
    verificacao_da_senha = input("Digite a senha: ")
    verificacao_do_id = input("Digite o id: ")
    while verificacao_da_senha != password:
        print("Senha incorreta")
        verificacao_da_senha = input("Tente novamente: ")
    while verificacao_do_id != id:
        print("Id incorreto")
        verificacao_do_id = input("Tente novamente: ")
    var_padrao = int(input("Digite o valor padrao: "))
    while var_padrao != var:
        print("Erro, valor errado, tente novamente")
        var_padrao = int(input("Digite o valor padrao: "))
    print("OK")
    tam_lista_criptografada = len(lista_com_a_frase_criptografada)
    for i in range(0,tam_lista_criptografada):
        texto_descriptografado = (lista_com_a_frase_criptografada[i]) - var
        frase_descriptografada = chr(texto_descriptografado)
        lista_com_a_frase_descpriptografada.append(frase_descriptografada)
        
    print(f"a frase criptografada foi {lista_com_a_frase_descpriptografada}")
    
    
else:
    print("Digite somente UM dos valores requeridos")