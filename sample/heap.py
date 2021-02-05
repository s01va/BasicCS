# -*- coding: utf-8 -*-

# 일반적으로 힙은 배열 자료구조를 활용.

# Max Heap

class Heap:
	def __init__(self., data):
		self.heap_array = list()
		self.heap_array = None
		self.heap_array.append(data)

	def pop(self):
		if len(self.heap_array) <= 1:
			return None

		returned_data = self.heap_array[1]
		