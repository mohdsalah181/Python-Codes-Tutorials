# Ask the user to enter statement
statement = input('please enter statement: ')

#seperate the words ------------------------------#
statementLength = len(statement)
words = []
word = ''
count = 0

for char in statement:
    if char == ' ':
        words.append(word)
        word=''
        count+=1
    elif count == statementLength-1:
        word= word + char
        words.append(word)
        
    else:
        word= word + char
        count+=1
    

#print the statment in reverse -------------------#
wordsCount = len(words)
while wordsCount:
    print(words[wordsCount-1], end=' ')
    wordsCount-=1
