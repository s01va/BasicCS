# -*- coding: utf-8 -*-

# Node 구현
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
"""
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