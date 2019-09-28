#Mariam Almalki
#LISTS

n = int(input('Enter number of commands: '))
LIST = []
for i in range(n):
    com = input('Enter the command: ')

    com = com.split()
    if com[0] == 'print':
        print(LIST)
    elif com[0] == 'sort':
        LIST.sort()
    elif com[0] == 'remove':
        com1 = int(com[1])
        LIST.remove(com1)
    elif com[0] == 'append':
        com1 = int(com[1])
        LIST.append(com1)
    elif com[0] == 'insert':
        com1 = int(com[1])
        com2 = int(com[2])
        LIST.insert(com1,com2)
    elif com[0] == 'reverse':
        LIST.reverse()
    elif com[0] == 'pop':
        LIST.pop()
