#İÇ İÇE FONKSİYONLAR

def factorial(number):

    if not number >= 0:
        raise Exception("Number must be an pozitif number") 

    if not isinstance(number,int):
        Exception("Number must be a number")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(6))