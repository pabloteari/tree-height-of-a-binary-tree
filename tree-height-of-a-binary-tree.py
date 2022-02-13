from classes.binarySearchTree import BinarySearchTree

tree = BinarySearchTree()

# Input number of nodes
inputNodesLimit = int(input())

# Input values nodes
arrayNodes = list(map(int, input().split()))

# Loop for number of nodes and create nodes
for i in range(inputNodesLimit):
    tree.create(arrayNodes[i])

# Print height
# print(tree.getHeight())
print(tree)