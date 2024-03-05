# Your own split
'''
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument - a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
'''

def mysplit(string):
    if string == '' or string.isspace():
        return [ ]
    list = []
    word = ''
    inword = not string[0].isspace()
    for char in string:
        if inword:
            if not char.isspace():
                word += char
            else:
                list.append(word)
                inword = False
        else:
            if not char.isspace():
                inword = True
                word = char
    if inword:
        list.append(word)
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))