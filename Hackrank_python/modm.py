#a, b, c = int(input()), int(input()), int(input())
#print(a**b)
#print(a**b%c)

#OR

a, b, c = [int(input()) for _ in '123'] # _ here implies that it takes the previous value that is here it is int(input())
#'123' here is similar to the range(3) it will simply execute the loop 3 times like the range function
print(pow(a,b), pow(a,b,c), sep = '\n')