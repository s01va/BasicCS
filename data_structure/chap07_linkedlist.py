# -*- coding: utf-8 -*-

# Node 구현
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

# Node와 Node 연결
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

#####################################

# Linked list로 데이터 추가하기

def add(data):
	node = head
	while node.next:
		node = node.next
	node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2, 10):
	add(index)

# Linked list 데이터 출력(검색)

node = head
while node.next:
	print(node.data)
	node = node.next
print(node.data)

# Node를 중간에 끼워넣기

node3 = Node(1.5)

node = head
search = True
while search:
	if node.data == 1:
		search = False
	else:
		node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
	print(node.data)
	node = node.next
print(node.data)

###################################################

# 파이썬 객체지향 프로그래밍으로 Linked list 구현

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class NodeMgmt:
	def __init__(self, data):
		self.head = Node(data)

	def add(self, data):
		if self.head == '':
			self.head = Node(data)
		else :
			node = self.head
			while node.next:
				node = node.next
			node.next = Node(data)

	def desc(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

	def delete(self, data):
		if self.head == '':
			print("해당 값을 가진 노드 없음.")
			return

		if self.head.data == data:	# self.head를 삭제해야 할 경우
			temp = self.head
			self.head = self.head.next
			del temp
		else:	# self.head가 아닌 노드를 삭제할 경우
			node = self.head
			while node.next:
				if node.next.data == data:
					temp = node.next
					node.next = node.next.next
					del temp
					return
				else:
					node = node.next

	def search_node(self, data):
		node = self.head
		while node:
			if node.data == data:
				return node
			else:
				node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,10):
	linkedlist1.add(data)
linkedlist1.desc()

print(linkedlist1.head)

linkedlist1.delete(0)
print(linkedlist1.head)
linkedlist1.delete(4)
linkedlist1.desc()

node = linkedlist1.search_node(5)
print(node.data)

#########################################

# double linked list

