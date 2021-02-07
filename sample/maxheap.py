# -*- coding: utf-8 -*-

# Max Heap

class Heap:
	def __init__(self., data):
		self.heap_array = list()
		self.heap_array = None
		self.heap_array.append(data)

	def move_down(popped_idx):
		left_child_popped_idx = popped_idx * 2
		right_child_popped_idx = popped_idx * 2 + 1

		if left_child_popped_idx >= len(self.heap_array):
			return False
		elif right_child_popped_idx >= len(self.heap_array):
			if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
				return True
			else:
				return False
		else:
			if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
				if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
					return True
				else:
					return False

	def pop(self):
		if len(self.heap_array) <= 1:
			return None

		returned_data = self.heap_array[1]
		self.heap_array = self.heap_array[-1]
		del self.heap_array[-1]
		popped_idx = 1

		while self.move_down(popped_idx):
			left_child_popped_idx = popped_idx * 2
			right_child_popped_idx = popped_idx * 2 + 1

			if right_child_popped_idx >= len(self.heap_array):
				if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
					self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
					popped_idx = left_child_popped_idx

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
			False

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