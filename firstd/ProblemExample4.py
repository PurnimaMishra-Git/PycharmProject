def is_palindrom(User_input):
    return str(User_input) == str(User_input)[::-1]

def is_palindrom_next(User_input):
    User_input = User_input + 1
    while not is_palindrom(User_input):
        User_input +=1
    return User_input



if __name__ == '__main__':
    size=int(input("enter size: "))
    num=[]
    for n in range(size):
        n1=int(input("Enter Element: "))
        num.append(n1)
    for n in range(size):
        print(f'For {num[n]} Palindrom is {is_palindrom(num[n])}')
        print(f'For {num[n]} Next Palindrom is {is_palindrom_next(num[n])}')


