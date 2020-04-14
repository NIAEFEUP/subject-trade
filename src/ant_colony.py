from graph import Graph
from node  import Node
from edge import Edge
from ant import Ant


# Create graph
g = Graph()

# Add initial node
g.add_root(Node(1,g.get_id()))

current_ant = Ant(1,1,g.root,g)
current_ant.expand_node()
print(str(g))
# Gerar ants



# Cada ant tem de decidir a ação

# Se expandir nó, acaba ant

# Se não, tem de escolher um nó para viajar, depositar as feromonas e dar update do node e voltar a decidir ação.