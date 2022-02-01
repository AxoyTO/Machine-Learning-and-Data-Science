def is_palindrome(x):
    tmp = x
    reverse_x = 0
    while(x > 0):
        dig = x % 10
        reverse_x = reverse_x*10+dig
        x = x//10
    if tmp == reverse_x:
        return "YES"
    else:
        return "NO"


print(is_palindrome(101))
