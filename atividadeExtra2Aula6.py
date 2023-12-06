print("Controle de estoque".upper())
 
def controle_de_estoque():
    produtos = []
    while True:
        aux = input("Insira o produtos. Ao finalizar digite 'Sair': ")
        produtos.append(aux)
        
        if(aux == "sair"):
          produtos.pop()
          print("Todas as suas mercadorias são: ", produtos)
          break
    print("No total suas mercadorias são: ", len(produtos))    
    
    try:
      auxiliar = input("Informe o nome do produto que deseja substituir(se não digite não): ")
      novo_prod = input("Agora informe o nome do produto que deseja colocar no lugar do informado (se não digite não) ")
      if(auxiliar != "não") and (novo_prod != "não"):
            for i in range(len(produtos)):
              if (produtos[i] == auxiliar):
                verif_posi = produtos.index(auxiliar)
                print(auxiliar, "está na posição: ", verif_posi)
                produtos[verif_posi] = novo_prod
              elif(auxiliar == "não") and (novo_prod == "não"):
                  print("Nenhuma substiuição foi feita")  
              if(len(auxiliar) == 0) or (len(novo_prod) == 0):
                 raise Exception("Algo deu errado, é provável que um dos dos campos esteja vazio")
    except Exception as err:
       print(err)
              
    try:
        verifica_nov_p = input("Se desejar inserir um novo produto ao final da lista informe o nome do produto aqui (se não digite não)  ")
        if(verifica_nov_p != "não") and (len(verifica_nov_p) != 0):
         produtos.append(verifica_nov_p)
        elif(verifica_nov_p == "não"):
         print("Nenhuma adição de novo produto foi feita!")
        if(len(verifica_nov_p) == 0):
         raise Exception("Algo deu errado, tente escrever tudo minusculo e não deixar nenhuma resposta vazia")
    except Exception as err:
     print(err)
     print("Por favor, siga todas as intruções como o programa pede")
   
    print("Lista de produtos atualizada: ", produtos)    

    print("No total suas mercadorias são: ", len(produtos))
    
controle  = controle_de_estoque()


