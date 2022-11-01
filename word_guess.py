import random

attempts = []
maxAttempts = 3

print(f'Welcome to the word_guessing game. Your max attempts to guess a single word: {maxAttempts}')

word_file = 'word_guess\words.txt'
words = open(word_file).read().splitlines()
word = random.choice(words)

money_file = 'money.txt'
money_file_element = open(money_file)
money = int(money_file_element.read()) or 0
money_file_element.close()

print(f'Your current cash: {money}')

def checkWord(nowWord):
    print(f'Your guess is: {nowWord}')
    global word
    global money

    if (nowWord.lower() == word.lower()):
        print('You guessed it, the game restarts.')
        attempts.clear()

        generateWord()
        money+= 100
        money_file_element = open(money_file, "w")
        money_file_element.write(str(money))
        money_file_element.close()
        print(f'Your current cash: {money}')
    elif (nowWord in attempts):
        print(f'You already tried the word {nowWord}, try a new one!')

        requestInput()

        return
    else:
        attempts.append(nowWord)

        print("You missed the word, try again!")
        print(f'Remaining attempts: {maxAttempts - len(attempts)}')

    if (len(attempts) >= maxAttempts):
        print("You couldn't guess the correct word, the game restarts with a new one!")
        attempts.clear()
        generateWord()

    requestInput()

def generateWord():
    global word 

    word = random.choice(words)

def requestInput():
    nowWord = input('Please enter a word! ')
    checkWord(nowWord)
requestInput()