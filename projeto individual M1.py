# Lista de resultados dos candidatos
#resultados = [
#"e4_t3_p5_s2",
#"e3_t4_p3_s4",
#"e5_t2_p4_s3",
#"e2_t5_p3_s5"
#]


def menu():
    print('ola, tudo bem? o que voce deseja fazer?')
    print('digite 0 para colocar novos candidatos ou')
    print('digite 1 para colocar os critérios e receber os resultados')
    resposta = input('     ')
    
    return resposta



#função para adicionar os candidatos
def adicionar_novo_candidato():

    candidatos = {}

    continuar = True

    while continuar:

        nome = input("Digite o nome do candidato: ")

        notas = []

        for etapa in ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]:

            nota = int(input(f"Insira nota {etapa} do candidato {nome} "))

            while nota > 10 or nota < 0:
                nota = int(input(f"Insira nota {etapa} do candidato {nome} "))
                
                
            notas.append(nota)

        str_notas = f'e{notas[0]}_t{notas[1]}_p{notas[2]}_s{notas[3]}'

        candidatos[nome] = str_notas

        resposta = input("Deseja adicionar outro aluno? (s/n): ")

        if resposta.lower() != 's':

            continuar = False

    return candidatos
    
    
    
    
# Função para buscar candidatos de acordo com os critérios
def buscar_candidatos(criterios,candidatos):
    
    lista_candidatos = candidatos.items()
    candidatos_compativeis = []
   
    
    for resultado in lista_candidatos:
        
        
            
        
        etapas = resultado[1].split("_")
        
        
        if all(int(etapa[1]) >= criterios[indice] for indice, etapa in enumerate(etapas)):
            candidatos_compativeis.append(resultado)
        
        
   
    
    return candidatos_compativeis
    
def solicita_criterio(candidatos):
    
     # Solicitar critérios ao usuário
    criterios = []
    print("Digite as avaliações mínimas desejadas para cada etapa (entrevista, teste teórico, teste prático, avaliação de soft skills):")
    for etapa in ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]:
        criterio = int(input(f"Avaliação mínima na {etapa}: "))
        criterios.append(criterio)

    # Buscar candidatos compatíveis
    candidatos_compativeis = buscar_candidatos(criterios,candidatos)

    # Exibir candidatos compatíveis
    if candidatos_compativeis:
        print("\nCandidatos compatíveis encontrados:")
    for candidato in candidatos_compativeis:
        print(candidato)
    else:
        print("\nNenhum candidato compatível encontrado.")
    
    


def main():
    
    
    
    candidatos = {'Gabriel': 'e2_t5_p6_s4', 'Matheus': 'e7_t5_p2_s6', 'Rodrigo': 'e5_t4_p9_s8'}
    #adicionar os candidatos e suas notas
    
    
    repeticao = True
    while repeticao:
        entrada = menu()
        if int(entrada) == 0:
            
        #adicionar mais candidatos ao dicionario 
            candidatos.update(adicionar_novo_candidato())
        else:
            repeticao = False
    
    solicita_criterio(candidatos)
    
    
    
    


main()