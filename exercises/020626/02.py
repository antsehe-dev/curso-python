# Create a Python function that takes an integer ( n ) as input
# and generates a dictionary containing pairs ( (i, i^2) ) for
# all integers ( i ) from 1 to ( n ) (inclusive). The function
# should then return this dictionary.

def generate_square_dict (n):
    print("{", end="")

    for i in range (1,n+1):
        print(f"{i}: {i*i}", end="")
        if(i!=n):
            print(", ", end="")
    print("}")
    
    
generate_square_dict(8)