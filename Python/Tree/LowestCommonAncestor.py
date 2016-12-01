class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# def lowest(root, first_value, second_value):
# 	first_search = []
# 	second_search = []
# 	found1 = False
# 	found2 = False
	
# 	def traverse(node, first_value):
# 		nonlocal first_search
# 		nonlocal found1
# 		if node == None or found1:
# 			return
		
# 		first_search.append(node.value)
# 		if node.value == first_value:
# 			found1 = True
# 		traverse(node.left, first_value)
# 		traverse(node.right, first_value)
# 		if not found1:
# 			first_search.pop()
# 	traverse(root, first_value)
# 	# print(first_search)

# 	def traverse(node, second_value):
# 		nonlocal second_search
# 		nonlocal found2
# 		if node == None or found2:
# 			return
		
# 		second_search.append(node.value)
# 		if node.value == second_value:
# 			found2 = True
# 		traverse(node.left, second_value)
# 		traverse(node.right, second_value)
# 		if not found2:
# 			second_search.pop()
# 	traverse(root, second_value)

# 	for i in range(len(second_search)):
# 		if second_search[i] in first_search:
# 			lowest_common_ancestor = second_search[i]

# 	return lowest_common_ancestor

def lowest(root, first_value, second_value):
	# first_search = []

	def traverse(node, search_value, array, found):
		if node == None:
			return
		elif found:
			print(array)
			return array
		else:
			array.append(node.value)
			if node.value == search_value:
				found == True
			traverse(node.left, search_value, array, found)
			traverse(node.right, search_value, array, found)
			if not found:
				array.pop()

	first_search = traverse(root, first_value, [], False)
	second_search = traverse(root, second_value, [], False)

	print(first_search)
	print(second_search)

	# for node in first_search:
	# 	print(node)
	# 	if node in second_search:
	# 		lowest_common_ancestor = node

	# return lowest_common_ancestor


def findPath(root, path, k):
 
    # Base Case
    if root is None:
        return False
 
    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.value)
 
    # See if the k is same as root's value
    if root.value == k :
        return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
      
    path.pop()
    return False
 
# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
 
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []
 
    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1 
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

a = Node(5)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(8)
f = Node(9)

a.left = b
a.right = c
c.left = d
c.right = e
e.right = f

# print(lowest(a, 4, 9))
print(findLCA(a, 4, 9))