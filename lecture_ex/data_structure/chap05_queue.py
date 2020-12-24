# -*- coding: utf-8 -*-

import queue

# 가장 일반적인 Queue(FIFO)
"""
data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
"""
# LIFO Queue(이거 스택 아님..?)
"""
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
"""
# PriorityQueue()
"""
data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))
# 앞의 숫자가 우선순위를 의미

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
"""
########################################

# 연습1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()

def enqueue(data):
	queue_list.append(data)

def dequeue():
	data = queue_list[0]
	del queue_list[0]
	return data

for i in range(10):
	enqueue(i)

print(len(queue_list))
print(dequeue())