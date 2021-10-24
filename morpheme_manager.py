word_list = []

while True:
    LANGUAGE_FILE = input("enter language file name: ")
    try:
        with open(LANGUAGE_FILE, 'r') as file:
            word_list = file.readlines()
        break
    except OSError:
        x = input("cannot open file, create new file? (y/n): ")
        if x == 'y':
            try:
                with open(LANGUAGE_FILE, 'w') as file:
                    pass
                break
            except OSError:
                print('failed to create file')
        elif x == 'n':
            exit()
        continue

COMMANDS = ['quit','list','find','add', 'remove', 'print', 'clear', 'similar']

# clean up list
for i in range(len(word_list)):
    word_list[i] = word_list[i].removesuffix('\n')
while '' in word_list:
    word_list.remove('')

# returns similar morphemes
def similar(word: str, words: list) -> list:
    similar_words = []
    for w in words:
        if word in w:
            similar_words.append(w)
    return similar_words

command = ''
while not command == 'quit':
    usr_in = input('enter command > ').split(' ')
    command = usr_in[0]
    if not command in COMMANDS:
        print('invalid command')
        continue
    elif command == 'list':
        print('\nMorpheme List:\n')
        for word in word_list:
            print(word)
        print()
    elif command == 'find':
        if len(usr_in) == 2:
            if usr_in[1] in word_list:
                print("'" + usr_in[1] + "' is in list")
            else:
                print("'" + usr_in[1] + "' is not in list")
        else:
            print('error: find takes 1 argument')
    elif command == 'add':
        if len(usr_in) == 2:
            if usr_in[1] in word_list:
                x = input("'" + usr_in[1] + "' is already in list, add anyway? (y/n): ")
                if not x == 'y':
                    continue
            similar_morphemes = similar(usr_in[1], word_list)
            if len(similar_morphemes) > 0:
                print("these similar morphemes already exist: ")
                for m in similar_morphemes:
                    print(m, end=' ')
                print()
                x = input("add '" + usr_in[1] + "' to list anyway? (y/n): ")
                if not x == 'y':
                    continue
            word_list.append(usr_in[1])
            print("added '" + usr_in[1] + "'")
        else:
            print('error: add takes 1 argument')
    elif command == 'remove':
        if len(usr_in) == 2:
            if usr_in[1] in word_list:
                word_list.remove(usr_in[1])
                print("removed '" + usr_in[1] + "'")
            else:
                print("error: '" + usr_in[1] + "' not in list")
        else:
            print('error: remove takes 1 argument')
    elif command == 'print':
        print(word_list)
    elif command == 'clear':
        x = input('are you sure you want to clear the list? (y/n): ')
        if x == 'y':
            word_list.clear()
    elif command == 'similar':
        if len(usr_in) == 2:
            similar_morphemes = similar(usr_in[1], word_list)
            print("these morphemes are similar: ")
            for m in similar_morphemes:
                print(m, end=' ')
            print()
        else:
            print('error: remove takes 1 argument')

with open(LANGUAGE_FILE, 'w') as file:
    for word in word_list:
        file.write(word + '\n')
