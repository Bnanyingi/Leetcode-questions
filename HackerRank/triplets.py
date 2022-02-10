from collections import Counter
# Complete the triplets function below.
def triplets(t, d):
   arr = 0
   
   #Fixing he first element
   for i in range(0, d-2):
    for j in range(i+1, d-1):
        for k in range(j+1,d):
            if(t[i] + t[j] + t[k]):
                arr+=1
            return arr
            
            
            

