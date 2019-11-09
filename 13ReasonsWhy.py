my_input = input().split()

A = int(my_input[0])
B = int(my_input[1])
C = int(my_input[2])

temp = A
A = B
B = temp

A = A*C
B = B+C

print(A,B)