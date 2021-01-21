# -*- coding: utf-8 -*-
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class NodeMgmt:
	def __init__(self, head):
		self.head = head

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
		if self.current_node.left == None and self.current_node.right == None:
			if value < self.parent.value:
				self.parent.left = None
			else:
				self.parent.right = None
		
		# Case 2
		elif self.current_node.left != None and self.current_node.right == None:
			if value < self.parent.value:
				self.parent.left = self.current_node.left
			else:
				self.parent.right = self.current_node.left
		elif self.current_node.left == None and self.current_node.right != None:
			if value < self.parrent.value:
				self.parent.left = self.current_node.right
			else:
				self.parent.right = self.current_node.right
		# Case 3
		elif self.current_node.left != None and self.current_node.right != None:
			# Case 3.1
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

		return True


##################################################3


import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)
    
# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)