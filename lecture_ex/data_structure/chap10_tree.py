# -*- coding: utf-8 -*-
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class NodeMgmt:
	def __init__(self, head):
		self.current_node = self.head

	def insert(self, value):
		self.current_node = self.head
		while True:
			if value < self.current_node.value:
				if self.current_node.left != None:
					self.current_node = self.current_node.left
				else:
					self.current_node.left = Node(value)
					break
			else:
				if self.current_node.right != None:
					self.current_node = self.current_node.right
				else:
					self.current_node.right = Node(value)
					break

	def search(self, value):
		self.current_node = self.head
		while self.current_node:
			if self.current_node.value == value:
				return True
			elif value < self.current_node.value:
				self.current_node = self.current_node.left
			else:
				self.current_node = self.current_node.right
		return False

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

BST.search(0)
BST.search(-1)

########################################

# 노드 삭제 - 경우를 나누어 생각하기

# Case 1: Leaf Node 삭제
# Case 2: Child Node가 하나인 Node 삭제
# Case 3: Child Node가 두개인 Node 삭제
#  Case 3.1: 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우

class NodeMgmt:
	# ...
	def delete(self, value):
		searched = False
		self.current_node = self.head
		self.parent = self.head
		while self.current_node:
			if self.current_node.value == value:
				searched = True
				break
			elif value < self.current_node.value:
				self.parent = self.current_node
				self.current_node = self.current_node.left
			else:
				self.parent = self.current_node
				self.current_node = self.current_node.right

		if searched == False:
			return False
		# Case 1
		# self.current_node가 삭제할 node, self.parent는 삭제할 Node의 Parent인 상태
		if self.current_node.left == None and self.current_node.right == None:
			if value < self.parent.value:
				self.parent.left = None
			else:
				self.parent.right = None
			del self.current_node
		
		# Case 2
		# 삭제할 Node가 child Node를 한 개 가지고 있음
		if self.current_node.left != None and self.current_node.right == None:
			if value < self.parent.value:
				self.parent.left = self.current_node.left
			else:
				self.parent.right = self.current_node.left
		elif self.current_node.left == None and self.current_node.right != None:
			if value < self.parrent.value:
				self.parent.left = self.current_node.right
			else:
				self.parent.right = self.current_node.right
		# Case 3.1
		# 삭제할 Node가 Parent Node 왼쪽에 있을 때
		# 전략1. 삭제할 Node의 right Child(s) 중, 가장 작은 값을 삭체할 Node의 Parent Node가 가리키게 함
		# 전략2. 삭제할 Node의 left Child(s) 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키게 함
		# 아래 구현은 전략 1임
		# 경우의 수는 두가지
		# 두 경우 모두 삭제할 Node가 Parent Node의 left에 있음
		#  Case 3.1.1
		#   삭제할 Node의 right Child(s) 중, 가장 작은 값을 가진 Node의 Child Node가 없음
		#  Case 3.1.2
		#   삭제할 Node의 right Child(s) 중, 가장 작은 값을 가진 Node의 right Child가 있음(가장 작은 값을 가졌기 때문에 left Child는 없음)
		if self.current_node.left != None and self.current_node.right != None:
			if value < self.parent.value:
				self.change_node = self.current_node.right
				self.change_node_parent = self.current_node.right
				while self.change_node.left != None:
					self.change_node_parent = self.change_node
					self.change_node = self.change_node.left
				if self.change_node.right != None: # Case 3.1.2
					self.change_node_parent.left = self.change_node.right
				else: # Case 3.1.1
					self.change_node_parent.left = None
				self.parent.left = self.change_node
				self.change_node.right = self.current_node.right
				self.change_node.left = self.current_node.left
		# Case 3.2
		# 삭제할 Node가 Parent Node 오른쪽에 있을 때
		# 전략1. 삭제할 Node의 right Child(s) 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 함
		# 전략2. 삭제할 Node의 left Child(s) 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키게 함
		# 아래 구현은 전략 1임
		# 경우의 수는 두가지
		# 두 경우 모두 삭제할 Node가 Parent Node의 right에 있음
		#  Case 3.2.1
		#   삭제할 Node의 right Child(s) 중, 가장 작은 값을 가진 Node의 Child Node가 있음
		#  Case 3.2.2
		#   삭제할 Node의 right Child(s) 중, 가장 작은 값을 가진 Node의 right Child가 있음
			else:
				self.change_node = self.current_node.right
				self.change_node_parent = self.current_node.right
				while self.change_node.left != None:
					self.change_node_parent = self.change_node
					self.change_node = self.schange_node.left
				if self.change_node.right != None: # Case 3.2.2
					self.change_node_parent.left = self.change_node.right
				else: # Case 3.2.1
					selc.change_node_parent.left = None
				self.parent.right = self.change_node
				self.change_node.left = self.current_node.left
				self.change_node.right = self.current_node.right