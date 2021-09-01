user_input = '112'
height = 6
#print(my_dict)
space = 4
one = '''
  *   
 **   
* *   
  *   
  *   
 ***  
          '''
A = '''
      *      
     * *     
    *   *    
   *******   
  *       *  
 *         * 
 '''
two = '''
   **   
 *   *  
     *  
    *   
   *    
  ***** 
   '''
my_dict = {}
my_dict['A'] = A
my_dict['1'] = one
my_dict['2'] = two
answer = ''
counter = 0
for i in my_dict:
    my_dict[i] = my_dict[i].split('\n')
for line in range(1,height+1):
    for shape in user_input:
        if shape in my_dict:
            answer += my_dict[shape][line]
    answer += '\n'
print(answer)


