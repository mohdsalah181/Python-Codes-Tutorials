# Ask the user to enter statement
statement = input('please enter statement: ')

#seperate the words ------------------------------#
statementLength = len(statement)
words = []
word = ''
count = 0

for i in statement:
    count = count+1
    word = word + i
    
    if i==' ' or count==statementLength:
        words.append(word)
        word = ''  
        
#print the statment in reverse -------------------#
wordsCount = len(words)
for i in range(wordsCount):
    print(words[wordsCount-1], end=" ")
    print(' ', end=" ")
    wordsCount-=1
