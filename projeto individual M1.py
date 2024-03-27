from tabulate import tabulate

def menu():
    print('\nOlá, tudo bem? O que você deseja fazer?')
    print('Digite 0 para adicionar novos candidatos.')
    print('Digite 1 para inserir critérios e obter resultados.')
    resposta = input('Digite a opção desejada: ')
    
    return resposta



#função para adicionar os candidatos
def adicionar_novo_candidato():

    candidatos = {}

    continuar = True

    while continuar:

        nome = input("\nDigite o nome do candidato: ")

        notas = []

        for etapa in ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]:

            nota = int(input(f"Insira nota {etapa} do candidato {nome}: "))

            while nota > 10 or nota < 0:
                nota = int(input(f"Insira nota {etapa} do candidato {nome}: "))
                
                
            notas.append(nota)

        str_notas = f'e{notas[0]}_t{notas[1]}_p{notas[2]}_s{notas[3]}'

        candidatos[nome] = str_notas

        resposta = input("Deseja adicionar outro aluno? (s/n): ")

        if resposta.lower() != 's':

            continuar = False

    return candidatos
    

# Solicitar critérios ao usuário
def solicita_criterio():
    
    
    criterios = []
    
    print("\nDigite as avaliações mínimas desejadas para cada etapa (entrevista, teste teórico, teste prático, avaliação de soft skills):")
    for etapa in ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]:
        criterio = int(input(f"Avaliação mínima na {etapa}: "))
        criterios.append(criterio)
    return criterios

    
    
# Função para buscar candidatos de acordo com os critérios
def buscar_candidatos(criterios,candidatos):
    
    lista_candidatos = candidatos.items()
    candidatos_compativeis = []
   
    
    for resultado in lista_candidatos:
        
        etapas = resultado[1].split("_")
        
        if all(int(etapa[1]) >= criterios[indice] for indice, etapa in enumerate(etapas)):
            candidatos_compativeis.append(resultado)
    
    return candidatos_compativeis



    


def mostra_resultado(resultado):
    
    # Exibir candidatos compatíveis como uma tabela
    if resultado:
        print("\nCandidatos compatíveis encontrados:")
        print(tabulate(resultado, headers=["Nome", "Notas"]))
    else:
        print("\nNenhum candidato compatível encontrado.")
    
    


def main():
    
    
    
    candidatos = {'Gabriel': 'e2_t5_p6_s4', 'Matheus': 'e7_t5_p2_s6', 'Rodrigo': 'e5_t4_p9_s8'}
    #adicionar os candidatos e suas notas
    
    while True:
        escolha = menu()
        
        if escolha == '0':
            novos_candidatos = adicionar_novo_candidato()
            candidatos.update(novos_candidatos)
            
        elif escolha == '1':
            criterios = solicita_criterio()
            resultado_candidatos = buscar_candidatos(criterios,candidatos)
            mostra_resultado(resultado_candidatos)
            break
            
            
        else:
            print('\nOpção inválida. Por favor, escolha 0 ou 1.')
    
    
    
    
    


main()
