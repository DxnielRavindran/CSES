
def Repetitions(n):
    ans, temp = 1, 1
    # Traverse the string
    for i in range(1, len(s)):
         
        # If character is same as
        # previous increment temp value
        if (s[i] == s[i - 1]):
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
 
    ans = max(ans, temp)
 
    # Return the required answer
    return ans
         



    

    
