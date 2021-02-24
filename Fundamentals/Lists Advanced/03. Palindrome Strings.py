word_list = input().split()
palindrome = input()
palindromes = []
[palindromes.append(pal) for pal in word_list if pal[::-1] == pal]
print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")

