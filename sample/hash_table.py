# -*- coding: utf-8 -*-

# Linear Probing 기법
# 폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
# 저장공간 활용도를 높이기 위한 기법

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

# 빈번한 해쉬 충돌 개선 -> 테이블 저장공간 늘리기

#############################################

# 연습4: 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘을 사용하도록 변경해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)

# 앞서 구현했던 Linear Probing을 수정

import hashlib

hash_table = list(0 for i in range(8))

def get_key(data):
	hash_object = hashlib.sha256()
	hash_object.update(data.encode())
	hex_dig = hash_object.hexdigest()
	return int(hex_dig, 16)

def hash_function(key):
	return key % 8

def save_data(data, value):
	index_key = get_key(data)
	hash_address = hash_function(index_key)
	if hash_table[hash_address] != 0:
		for index in range(hash_address, len(hash_table)):
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

print (get_key('db') % 8)
print (get_key('da') % 8)
print (get_key('dh') % 8)
