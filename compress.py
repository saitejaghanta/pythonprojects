inp = input("enter any string to compress: ")
count = 1
for i in range(1, len(inp) + 1):
    if i == len(inp):
        print(inp[i - 1] + str(count), end="")
        break
    else:
        if inp[i - 1] == inp[i]:
            count += 1
        else:
            print(inp[i - 1] + str(count), end="")
            count = 1
