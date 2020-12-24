# -*- coding: utf-8 -*-

data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 연습1: 위의 2차원 배열에서 9, 8, 7 을 순서대로 출력해보기

for member in reversed(data_list[2]):
	print(member)

##########################################################################

dataset = ['Braund, Mr. Owen Harris',
	'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
	'Heikkinen, Miss. Laina',
	'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
	'Allen, Mr. William Henry',
	'Moran, Mr. James',
	'McCarthy, Mr. Timothy J',
	'Palsson, Master. Gosta Leonard',
	'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
	'Nasser, Mrs. Nicholas (Adele Achem)',
	'Sandstrom, Miss. Marguerite Rut',
	'Bonnell, Miss. Elizabeth',
	'Saundercock, Mr. William Henry',
	'Andersson, Mr. Anders Johan',
	'Vestrom, Miss. Hulda Amanda Adolfina',
	'Hewlett, Mrs. (Mary D Kingcome) ',
	'Rice, Master. Eugene',
	'Williams, Mr. Charles Eugene',
	'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
	'Masselmani, Mrs. Fatima',
	'Fynney, Mr. Joseph J',
	'Beesley, Mr. Lawrence',
	'McGowan, Miss. Anna "Annie"',
	'Sloper, Mr. William Thompson',
	'Palsson, Miss. Torborg Danira',
	'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
	'Emir, Mr. Farred Chehab',
	'Fortune, Mr. Charles Alexander',
	'Dwyer, Miss. Ellen "Nellie"',
	'Todoroff, Mr. Lalio']

# 연습2: 위의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기

Mnum = 0

for member in dataset:
	for ch in member:
		if ch == 'M':
			Mnum += 1
print(Mnum)