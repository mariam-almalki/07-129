num = int(input("enter number of words: "))
LIST = []
for i in range(num):
    word = input("enter word: ")
    LIST.append(word)
frequency = []
for j in range(len(LIST)):
    
    for LIST[j] in LIST:
        frequency.append(LIST[j])
        print(len(frequency),'\n')
        j +=1
