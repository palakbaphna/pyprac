print("*Multiplication Example*")

print("a = ")

a= int(input())

print("b = ")
b = int(input())

print("c = ")
c = int(input())

answer = a * b * c

print( 'The answer of a*b*c = ' , answer )

if( answer > 100):                                                      #or if( a * b * c > 100)
    print( "Answer is greater than 100" )
else:
    print("Answer is not greater than 100")
