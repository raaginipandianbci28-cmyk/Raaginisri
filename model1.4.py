s = input("Enter the string to compress: ")
compressed = ""
count = 1
if s:
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
print("Compressed output:", compressed)
