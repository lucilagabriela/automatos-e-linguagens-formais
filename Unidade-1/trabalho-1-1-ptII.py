print("=========================================================")
print("Autômatos e Linguagens Formais - DCA-3705")
print("1a Lista de Programação - Máquina de Estados Finitos")
print("=========================================================\n")

'''
ni, no, ns: número de entradas, saídas e estados
I vetor de entrada
O vetor de saída
s0, s1, s2: estados da máquina de estados com índices 0, 1 e 2

TE: Tabela de Transição de Estados
      0   1 (entradas)
s0    n1  n0
s1    n2  n1
s2    n2  n0
TE[ns+1, ni+1]

VS: Vetor de Saída
so -> 0,
s1 -> 1,
s2 -> 1
VS[no+1]
'''

# Para a máquina de estados do PDF:

# Definindo o tamanho da máquina
ni = 1 # I = {0, 1}
no = 1 # O = {0, 1}
ns = 2 # estados = s0, s1 e s2

# Tabela de Transição de Estados --> TE[estado][entrada] = próximo estado
TE = [
    [0, 1],   # s0
    [0, 2],   # s1
    [0, 2],   # s2
]

# Vetor de Saída --> VS[estado] = saída daquele estado
VS = [0, 0, 1] # so = 0, s1 = 1, s2 = 1

# Definindo o início da máquina
estadoInicial = 0
estadoAtual = estadoInicial

print("A máquina de estados finito foi iniciada no estado s" + str(estadoAtual), "-- saída:", VS[estadoAtual])
print("Digite 0 ou 1 para uma entrada, 'sair' para interromper a simulação ou 'r' para reset.")

while True:
  entrada = input("Entrada: ").strip()

  if entrada == "sair":
    print("Simulação encerrada.")
    break

  if entrada == 'r':
    estadoAtual = estadoInicial
    print("[RESET] estado: s" + str(estadoAtual), "-- saída:", VS[estadoAtual])

  elif entrada.isdigit() and int(entrada) <= ni:
    entrada = int(entrada)
    estadoAtual = TE[estadoAtual][entrada]
    print("estado: s" + str(estadoAtual), "-- saída:", VS[estadoAtual])

  else:
    print("Entrada inválida! Use apenas valores de 0 a", ni, "ou 'r'.")
