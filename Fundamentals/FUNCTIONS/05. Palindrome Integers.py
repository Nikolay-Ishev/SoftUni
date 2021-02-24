def palindrome_integers(a):
    for element in a:
        mid_len = len(element) // 2
        if len(element) % 2 != 0:
            str1 = element[:mid_len]
            str2 = element[mid_len + 1:]
        else:
            str1 = element[:mid_len]
            str2 = element[mid_len:]
        txt = str2[::-1]
        if txt == str1:
            print("True")
        else:
            print("False")


int_list = input().split(", ")
palindrome_integers(int_list)

#можеше просто да попитам дали ( element = element[::-1] )
