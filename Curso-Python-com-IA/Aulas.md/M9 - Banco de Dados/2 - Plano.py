# PLANO DO PROJETO CRUD: LISTA DE TAREFAS

"""

INTERFACE:

- Frame principal:
    - Entrada de nova tarefa (enter para adicionar)
    - Lista de tarefas

- Frame lateral esquerda:
    - Botão para aba arquivadas
    - Botão para aba lixeira

-----------------
|    |
| fl |    fp
|    |
-----------------

fp = frame principal
fl = frame lateral esquerda


Janela no geral:
    - Vai abrir no meio da tela
    - Vai estar maximizada
    - Vai ter a largura e altura da tela do dispositivo
    - Vai ter o título "Clone google keep"
    - Ver ter o tema dark mode

dentro do fp:
    - Separar em 2 frames:
        - frame de entrada de tarefa:
            - Fixado na parte superior e tomando o espaço de uma linha
        - frame de lista de tarefas:
            - Fixado na parte central
            - Lista de tarefas
            - Vai ser um frame scrollable

dentro do fl:
    - Botão para aba arquivadas (com ícone de arquivo)
    - Botão para aba lixeira (com ícone de lixeira)
    - Os dois botões vão estar fixados na parte superior e ocupando o espaço de uma linha cada (layout pack, ou seja, um embaixo do outro)


Visualização das tarefas:
    - Cada tarefa vai ter um botão de "x" para deletar
    - Cada tarefa vai ter um botão de "arquivar"
    - E um checkbox para marcar como concluída

Visualização das abas:
    - Aba "Todas as tarefas" (ativa por padrão)
    - Aba "Arquivadas"
    - Aba "Lixeira"

Aba "Lixeira":
    - A lixeira vai ter uma lista de tarefas deletadas
    - Cada tarefa deletada vai ter um botão para restaurar

Aba "Arquivadas":
    - A aba arquivadas vai ter uma lista de tarefas arquivadas
    - Cada tarefa arquivada vai ter um botão para desarquivar
    
--------------------------------

FUNCIONALIDADES:

Usar o banco de dados sqlite3 para armazenar as tarefas

- Adicionar tarefa:
    - Ao digitar e dar enter, a tarefa é adicionada à lista de tarefas
    - A nova tarefa será adicionada no topo da lista

- Deletar tarefa:
    - Ao clicar no botão "x", a tarefa será deletada (ou seja, removida da lista) e enviada para a lista da aba lixeira, com a data e hora exatas em que foi deletada

- Arquivar tarefa:
    - Ao clicar no botão "arquivar", a tarefa será arquivada (ou seja, removida da lista e enviada para a lista da aba arquivadas)

- Marcar como concluída:
    - Ao clicar no checkbox, a tarefa será marcada como concluída: checkbox ficará marcado e o texto da tarefa ficará com a cor cinza e com uma linha no meio

Pontos de Atenção:
    - Ao acessar a aba lixeira, as tarefas não vão ter checkbox de conclusão, e as tarefas com mais de 3 dias desde que foram deletadas vão ser excluídas automaticamente (verificar isso sempre que acessar a aba lixeira)
    

"""