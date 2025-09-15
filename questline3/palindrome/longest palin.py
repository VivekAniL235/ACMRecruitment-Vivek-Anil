s = input('enter the string')

longest_palindrome = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
        
        is_palindrome = True
        if substring != substring[::-1]:
            is_palindrome = False

        if is_palindrome and len(substring) > len(longest_palindrome):
            longest_palindrome = substring

print(f"The longest palindromic substring in '{s}' is: '{longest_palindrome}'")
