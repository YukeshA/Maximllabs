def unique_count(st):
    unique = []
    for char in st[::]:
        if char not in unique:
            unique.append(char)
    return len(unique)

def length_smallest_sub(s):
    n = len(s)
    d = {}
    for i in range(n):
        for j in range(i,n+1):
            sub = s[i:j]
            unique_count(sub)
            d[sub] = unique_count(sub)
    ls = sorted(d.items(), key=lambda x:x[1],reverse=True)
    maxm = ls[0][1]
    length = len(ls[0][0])
    for x in ls:
        if x[1] == maxm:
            # print(x[1])
            # print(x[0])
            n = len(x[0])
            if n<length:
                length = n
    return length

if __name__ == "__main__":
    s = input("Enter the string:")
    length = length_smallest_sub(s)
    print("Length of the smallest substring with maximum distinct character:{0}".format(length))
