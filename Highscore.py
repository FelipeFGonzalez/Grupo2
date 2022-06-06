
def insereScore(nomeJogo, nomeUsuario, pontuacao):
    listaLinhas = []
    novaPosicao = 1
    contador = 1
    arquivoCriacao = open("Score_" + nomeJogo + ".txt", "a")
    arquivoCriacao.close()
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        for linha in arquivo:
            contador += 1 
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                contador -= 1
                if pontuacao < linhaScore[2]:
                    return
            else:
                listaLinhas.append(linhaScore)
            
            if linhaScore[2] > pontuacao:
                novaPosicao += 1
    
    if novaPosicao > 1024:
        return
    if contador > 1024:
        contador = 1024
    listaLinhas.insert(novaPosicao - 1 , [str(novaPosicao), nomeUsuario, pontuacao])
    print(listaLinhas)

    with open("Score_" + nomeJogo + ".txt", "w") as arquivoSaida:
        for i in range(contador):
            arquivoSaida.write(str(i + 1) + " " + listaLinhas[i][1] + " " + listaLinhas[i][2] + "\n")

    return



def buscaScore(nomeJogo, nomeUsuario):
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        for linha in arquivo:
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                return linhaScore
                



def removeScore(nomeJogo, nomeUsuario):
    contador = 0
    listaLinhas = []
    usuarioEncontrado = 0
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        for linha in arquivo:
            contador += 1 
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                usuarioEncontrado = 1
            else:
                listaLinhas.append(linhaScore)

    if usuarioEncontrado == 0:
        return
    else:
        with open("Score_" + nomeJogo + ".txt", "w") as arquivoSaida:
            for i in range(contador - 1): ##CONFERIR -1
                arquivoSaida.write(str(i + 1) + " " + listaLinhas[i][1] + " " + listaLinhas[i][2] + "\n")
    return
    
    
    
def top10(nomeJogo):
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        listatop10 = []
        cont = 0
        for linha in arquivo:
            linhaScore = (linha.strip()).split(" ")
            if cont < 10:
                listatop10.append(linhaScore)
            else:
                break
    return listatop10
    

