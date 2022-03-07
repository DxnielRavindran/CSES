
from doctest import master

def TwoSets(n):
    nope = "NO"
    yes = "YES"
    master = []
    set = []
    answer = []
    reversed = []
    sum = 0
    count = 1
    
    # 7 =  1+2+3+4+5+6+7 = 28 (14) = yes | 7 + 6 + 1 AND 5 + 4 + 3 + 2

    # 8 =  1+2+3+4+5+6+7+8 = 36 (18) = yes | 8 + 7 + 1 + 2 AND 3 + 4 + 5 + 6 

    # 9 = 1+2+3+4+5+6+7+8+9 = NO

    # 11 = 1+2+3+4+5+6+7+8+9+10+11 = 66 (33) = yes | 11 + 10 + 9 + 1 + 2 AND 3 + 4 + 5 + 6 + 7 + 8

    # getting master set
    for each in range(n):
        sum  += count
        master.append(count)
        count +=1  

    if sum%2 == 0:
        answer.append(yes)    
        half = sum / 2
        reversed = master[::-1]
        sum = 0
        
        #finding first set of combinations
        for each in reversed:
            if sum + each <= half:
                set.append(each)
                sum += each
                
        answer.append(len(set))
        answer.append(set)

        for each in set:
            if each in master:
                master.remove(each)                
        answer.append(len(set))
        answer.append(set)
        print(answer)

    else:
        print(nope)
    


TwoSets(7)


   

         



    

 