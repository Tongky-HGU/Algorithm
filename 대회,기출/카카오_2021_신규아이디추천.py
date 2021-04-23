#신규아이디 추천
def solution(new_id):
    check = ['-','_','.']
    
    #1
    new_id = new_id.lower()
    
    #2
    temp = []
    for char in new_id:
        for i in check:
            if char == i:
                temp.append(char)
                break
        if char.isalpha() or char.isdigit():
            temp.append(char)
    new_id = ''.join(temp)
         
    #3
    temp =[]
    flag = 0
    for char in new_id:
        if char == '.':
            if flag == 0:
                temp.append(char)
                flag = 1
        else:
            temp.append(char)
            flag = 0
    
    #4
    if len(temp) > 0 and temp[0] == '.':
        del temp[0]
    if len(temp) and temp[-1] == '.':
        del temp[-1]
        
    #5
    if len(temp) == 0:
        temp.append('a')
        
    #6 
    if len(temp) >= 16:
        temp= temp[:15]
        if temp[-1] == '.':
            del temp[-1]
    # #7
    elif len(temp) < 3:
        while(len(temp) < 3):
            temp.append(temp[-1])
    
    return ''.join(temp)