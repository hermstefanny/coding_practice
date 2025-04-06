def isPalindrome(s: str) -> bool:

    is_pal = False
    pal = [char.lower() for char in s if char.isalnum()]
    print(pal)

    i = 0
    j = len(pal) - 1

    while i < len(pal) and j >= 0:

        if pal[i] != pal[j]:
            return False

        j -= 1
        i += 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))
