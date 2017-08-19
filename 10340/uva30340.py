from sys import stdin

def subseq(a,b):
    la, lb = len(a) ,len(b)
    i, j = 0, 0
    if lb<la:
        return False

    while True:
        if i == la or j == lb:
            break

        if a[i] == b[j]:
            i+=1
        j+=1

    return i == la



if __name__ == '__main__':
    
    line = stdin.readline()
    while line:
        line = line[:-1].split()
        res = subseq(line[0], line[1])
        resa = 'Yes' if res else 'No'  
        print(resa)
        line = stdin.readline()
    None


