# i=0
# j=0 
# while i<10:
#     for j in range(i):
#         print(' ', end = "")
#     for j in range(10-i):
#         print('*', end = "")
#     j=j+1    
#     print(" ")
#     i= i+1
    
i=0
j=10 
while i<10:
    print(' '*i, end="")
    print('*'*j, end = "")
    j=j-1    
    print()
    i= i+1