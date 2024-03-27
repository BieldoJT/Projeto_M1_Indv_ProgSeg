# Projeto_M1_Indv_ProgSeg

# Sistema de Gerenciamento de Candidatos

Este é um sistema simples de gerenciamento de candidatos, onde você pode adicionar novos candidatos com suas respectivas notas em diferentes etapas e, em seguida, buscar candidatos com base em critérios específicos.

## Funcionalidades

- Adicionar novos candidatos com suas notas em entrevista, teste teórico, teste prático e avaliação de soft skills.
- Buscar candidatos compatíveis com critérios mínimos definidos pelo usuário.

## Instalação

Certifique-se de ter o Python instalado em sua máquina. Este código foi testado com Python 3. Se você ainda não tem o `tabulate` instalado, você pode instalá-lo usando o seguinte comando:

## Uso

Execute o arquivo `sistema_gerenciamento_candidatos.py` para iniciar o programa. Você será apresentado a um menu com duas opções:

1. **Adicionar Novos Candidatos:** Permite adicionar novos candidatos com suas respectivas notas.
2. **Inserir Critérios e Obter Resultados:** Permite inserir critérios mínimos desejados para cada etapa e obter uma lista de candidatos compatíveis.

Siga as instruções apresentadas no menu para interagir com o programa.

## Exemplo

Aqui está um exemplo de uso do programa:

1. Adicionar novos candidatos:
   - Nome: Maria
     - Entrevista: 8
     - Teste Teórico: 7
     - Teste Prático: 9
     - Avaliação de Soft Skills: 6
   - Nome: João
     - Entrevista: 6
     - Teste Teórico: 8
     - Teste Prático: 7
     - Avaliação de Soft Skills: 5

2. Inserir critérios e obter resultados:
   - Avaliação mínima na Entrevista: 7
   - Avaliação mínima no Teste Teórico: 7
   - Avaliação mínima no Teste Prático: 7
   - Avaliação mínima na Avaliação de Soft Skills: 7

   Resultado:

      Nome  | Notas
      ------|---------------
      Maria | e8_t7_p9_s6
      João  | e6_t8_p7_s5

