import textwrap

def wrap(string, max_width):
    newtext=""
    for i in range(0,len(string),max_width):
        newtext+=string[i:i+max_width]+'\n'
    return newtext

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
