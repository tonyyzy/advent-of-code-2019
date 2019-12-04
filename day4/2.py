def adj(num):
    num = str(num)
    if num[0] == num[1] and num[1] != num[2]:
        return True
    if num[-1] == num[-2] and num[-3] != num[-2]:
        return True
    for i in range(1, len(num) - 2):
        if num[i] == num[i+1] and num[i] != num[i-1] and num[i+1] != num[i+2]:
            return True
    return False

def dec(num):
    num = str(num)
    if int(num[0]) <= int(num[1]) and \
        int(num[1]) <= int(num[2]) and \
        int(num[2]) <= int(num[3]) and \
        int(num[3]) <= int(num[4]) and \
        int(num[4]) <= int(num[5]):
        return True
    else:
        return False

if __name__ == "__main__":
    acceptable = []
    for password in range(273025, 767254):
        if adj(password) and dec(password):
            acceptable.append(password)
    print(len(acceptable))
        