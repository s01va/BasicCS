# -*- coding: utf-8 -*-

#hash_table = list([0 for i in range(10)])
hash_table = list([i for i in range(10)])
print(hash_table)

def hash_func(key):
	return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

# ord(str) : str의 ascii return
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))
print(ord(data1[0]), ord(data4[0]))

def storage_data(data, value):
	key = ord(data[0])
	hash_address = hash_func(key)
	hash_table[hash_address] = value

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

def get_data(data):
	key = ord(data[0])
	hash_address = hash_func(key)
	return hash_table[hash_address]

print(get_data('Andy'))

##########################################################

# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)

hash_table = list(0 for i in range(8))

def get_key(data):
	return hash(data)

def hash_function(key):
	return key % 8

def save_data(data, value):
	hash_address = hash_function(get_key(data))
	hash_table[hash_address] = value

def read_data(data):
	hash_address = hash_function(get_key(data))
	return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
read_data('Dave')

print(hash_table)

#############################################################

# Chaining 기법

# 연습2: 연습1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)

hash_table = list(0 for i in range(8))

def get_key(data):
	return hash(data)

def hash_function(key):
	return key % 8

def save_data(data, value):
	index_key = get_key(data)
	hash_address = hash_function(index_key)
	if hash_table[hash_address] != 0:
		for index in range(len(hash_table[hash_address])):
			if hash_table[hash_address][index][0] == index_key:
				hash_table[hash_address][index][1] = value
				return
	else:
		hash_table[hash_address] = [[index_key, value]]

def read_data(data):
	index_key = get_key(data)
	hash_address = hash_function(get_key(data))

	if hash_table[hash_address] != 0:
		for index in range(len(hash_table[hash_address])):
			if hash_table[hash_address][index][0] == index_key:
				return hash_table[hash_address][index][1]
		return None
	else:
		return None

print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')

print(hash_table)

#############################################

# Linear Probing 기법

# 연습3: 연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)

hash_table = list(0 for i in range(8))

def get_key(data):
	return hash(data)

def hash_function(key):
	return key % 8

def save_data(data, value):
	index_key = get_key(data)
	hash_address = hash_function(index_key)
	if hash_table[hash_address] != 0:
		for index in range(hash_address, len(hash_table )):
			if hash_table[index] == 0:
				hash_table[index] = [hash_address, value]
				return
			elif hash_table[index][0] == index_key:
				hash_table[index][1] = value
				return
	else:
		hash_table[hash_address] = [index_key, value]

def read_data(data):
	index_key = get_key(data)
	hash_address = hash_function(index_key)

	if hash_table[hash_address] != 0:
		for index in range(hash_address, len(hash_table)):
			if hash_table[index] == 0:
				return None
			elif hash_table[index][0] == index_key:
				return hash_table[index][1]
	else:
		return None

print (hash('dk') % 8)
print (hash('da') % 8)
print (hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
read_data('dc')