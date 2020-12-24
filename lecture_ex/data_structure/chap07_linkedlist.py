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

# Doubly linked list

class Node:
	def __init__(self, data, prev=None, next=None):
		self.prev = prev
		self.data = data
		self.next = next

class NodeMgmt:
	def __init__(self, data):
		self.head = Node(data)
		self.tail = self.head

	def insert(self, data):
		if self.head == None:
			self.head = Node(data)
			self.tail = self.head
		else:
			node = self.head
			while node.next:
				node = node.next
			new = Node(data)
			node.next = new
			new.prev = node
			self.tail = new

	def desc(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

	def search_from_head(self, data):
		if self.head == None:
			return False

		node = self.head
		while node:
			if node.data == data:
				return node
			else:
				node = node.next

			return False

	def search_from_tail(self, data):
		if self.head == None:
			return False

		node = self.tail
		while node:
			if node.data == data:
				return node
			else:
				node = node.prev

		return False

	def insert_before(self, data, before_data):
		if self.head == None:
			self.head = Node(data)
			return True
		else:
			node = self.tail
			while node.data != before_data:
				node = node.prev
				if node == None:
					return False
			new = Node(data)
			before_new = node.prev
			before_new.next = new
			new.prev = before_new
			new.next = node
			node.prev = new
			return True


double_linkedlist = NodeMgmt(0)

for data in range(1, 10):
	double_linkedlist.insert(data)

double_linkedlist.desc()

node_3 = double_linkedlist.search_from_tail(3)
print(node_3.data)

double_linkedlist.insert_before(1.5, 2)
double_linkedlist.desc()

node_3 = double_linkedlist.search_from_tail(1.5)
print(node_3.data)

######################################################

# 노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수를 만들고, 테스트해보기
# - 더블 링크드 리스트의 head 에서부터 다음으로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
# - 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 1인 노드 다음에 1.7 데이터 값을 가진 노드를 추가해보기

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next


node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.insert(data)

node_mgmt.desc()

node_mgmt.insert_after(1.5, 1)
node_mgmt.desc()