#  voh saari lists print krni hai jinka sum n nhi ho

if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    n = int(input("Enter n: "))

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

    print(result)



# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort(reverse=True)
    
#     scores = [item for index, item in enumerate(arr) if item not in arr[:index]]
#     print(scores[1])
    


    