'''Searches through file for certain word'''


def word_find():
    try:
        filename = input('Enter name of file: ')
        search = input('Enter the word you are searching for: ')

        with open(filename, 'r') as f_obj:
            
            count = 0
            lines = f_obj.readlines()
            for line in lines:
                if search in line: #or line.startswith(search):
                    print(line)
                    count += 1
                else:
                    continue
            print('----------------')
            print(search, 'appeared ' + str(count) + ' times in this file.')    
    except FileNotFoundError:
        print('File not found.')
        word_find()

word_find()

