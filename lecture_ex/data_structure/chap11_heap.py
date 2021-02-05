# -*- coding: utf-8 -*-

# 일반적으로 힙 구현시 배열 자료구조를 활용함
# (구현의 편의를 위해, 인덱스 1번부터)

# 다음 구현 예시는 Max heap

class Heap:
	def __init__(self, data):
		self.heap_array = list()
		self.heap_array.append(None) # [0]
		self.heap_array.append(data) # [1]

	# insert 1
	def insert(self, data):
		if len(self.heap_array) == 0:
			self.heap_array.append(None) # [0]
			self.heap_array.append(data) # [1]
			return True

		self.heap_array.append(data)
		return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)


# insert2
# 삽입한 노드가 부모 노드의 값보다 클 때, 부모 노드와 삽입한 노드 위치를 바꾼다.
# 삽입한 노드가 루트 노드가 되거나, 부모 노드보다 값이 작거나 같을 때까지 반복

# move_up 함수 추가

class Heap:
	def __init__(self, data):
		self.heap_array = list()
		self.heap_array.append(None) # [0]
		self.heap_array.append(data) # [1]

	def move_up(self, inserted_idx):
		if inserted_idx <= 1:
			return False

		parent_idx = inserted_idx // 2

	def insert(self, data):
		if len(self.heap_array) == 0:
			self.heap_array.append(None) # [0]
			self.heap_array.append(data) # [1]
			return True

		self.heap_array.append(data)
		inserted_idx = len(self.heap_array) - 1

		while self.move_up(inserted_idx):
			parent_idx = inserted_idx // 2
			self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
			inserted_idx = parent_idx

		return True

# 데이터 삭제 구현
# delete1: 보통 삭제는 최상단 노드를 삭제하는 것이 일반적임. -> pop함수
class Heap:
	def __init__(self, data):
		self.heap_array = list()
		self.heap_array.append(None)
		self.heap_array.append(data)

	def pop(self):
		if len(self.heap_array) <= 1:
			return None

		returned_data = self.heap_array[1]
		return returned_data

# delete2: 상단 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로, 가장 마지막에 추가한 노드)를 root로 이동시킴.
# root 노드의 값이 child node보다 작으면, root node의 child 중 가장 큰 값을 가진 노드와 root node 위치를 바꿔주는 작업을 반복한다.(swap)

# 특정 노드의 관련 노드 위치 알아내기
## parent node index = child node index // 2
## left child index = parent node index * 2
## right child index = parent node index * 2 + 1
# ㄴ이것이 Heap의 핵심

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.heap_array

print(heap.pop()) # 20

####################################################

class Heap:
	def __init__(self, data):
		self.heap_array = list()
		self.heap_array.append(None)
		self.heap_array.append(data)

	def move_down(self, popped_idx):
		left_child_popped_idx = popped_idx * 2
		right_child_popped_idx = popped_idx * 2 + 1
		# Case1: left child '도' 없을 때
		if left_child_popped_idx >= len(self.heap_array):
			return False
		# Case2: right child만 없을 때
		elif right_child_popped_idx >= len(self.heap_array):
			if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
				return True
			else:
				return False
		# Case3: left, right child 둘 다 있을 때
		else:
			if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
				if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
					return True
				else:
					return False
				else:
					if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
						return True
					else:
						return False

	def pop(self):
		if len(self.heap_array) <= 1:
			return None

		returned_data = self.heap_array[1]
		self.heap_array[1] = self.heap_array[-1]
		del self.heap_array[-1]
		popped_idx = 1

		while self.move_down(popped_idx):
			left_child_popped_idx = popped_idx * 2
			right_child_popped_idx = popped_idx * 2 + 1

			# Case2: 오른쪽 자식 노드만 없을 때
			if right_child_popped_idx >= len(self.heap_array):
				if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
					self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
					popped_idx = left_child_popped_idx

			# Case3: left, right child 둘 다 있을 때
			else:
				if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
					if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
						self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
						popped_idx = right_child_popped_idx
					else:
						if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
							self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
							popped_idx = right_child_popped_idx

		return returned_data

	def move_up(self, inserted_idx):
		if inserted_idx <= 1:
			return False
		parent_idx = inserted_idx // 2
		if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
			return True
		else:
			return False

	def insert(self, data):
		if len(self.heap_array) == 1:
			self.heap_array.append(data)
			return True

		self.heap_array.append(data)
		inserted_idx = len(self.heap_array) - 1

		while self.move_up(inserted_idx):
			parent_idx = inserted_idx // 2
			self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
		return True