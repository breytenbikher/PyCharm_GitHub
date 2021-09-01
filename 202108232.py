height = 3
spacing = 4
string_1 ='''
***
* *
***
'''
string_2 = '''
* *
 * 
* *
'''
string_3 = '''
 * 
***
 * 
'''	
str_dict = {}
str_dict[1] = string_1
str_dict[2] = string_2
str_dict[3] = string_3
for i in str_dict:
	str_dict[i] = str_dict[i].split('\n')
answer = ''
for line in range(1,height+1):
	for number_of_shape in [1,2,3]:
		answer += str_dict[number_of_shape][line] + ' '*spacing
	answer += '\n'
print(answer)