def adj(num):
    num = str(num)
    if num[0] == num[1] or \
        num[1] == num[2] or \
        num[2] == num[3] or \
        num[3] == num[4] or \
        num[4] == num[5]:
        return True
    else:
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
        