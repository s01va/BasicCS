# -*- coding: utf-8 -*-

def recursive(data):
	if data < 0:
		print("End")
	else:
		print(data)
		recursive(data - 1)
		print("return ", data)

recursive(10)

######################################

# list 사용 시 append(), pop() 사용

stack_list = list()

def push(data):
	stack_list.append(data)
def pop():
	data = stack_list[-1]
	del stack_list[-1]
	return data

for index in range(10):
	push(index)

print(pop())