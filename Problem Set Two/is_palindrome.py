# Checks if a string is a palindrome or not

def isPalindrome(s: str) -> bool:
    if(s == "" or len(s) == 1):
        return True
    elif(s[0] == s[-1]):
        return isPalindrome(s[1: len(s) -1])
    else:
        return False


print(str(isPalindrome("1000021")))