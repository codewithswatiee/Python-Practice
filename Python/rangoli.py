def rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    lines = []
    width = (size - 1) * 4 + 1
    
    for i in range(size):
        left = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        line = left.center(width, '-')
        lines.append(line)
    
    result = '\n'.join(lines[::-1] + lines[1:])
    return result

# Test the function
size = int(input("Enter the size of the rangoli: "))
print(rangoli(size))
