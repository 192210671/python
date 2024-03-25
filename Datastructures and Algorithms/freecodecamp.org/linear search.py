
def locate_card(cards,query):
    position=0
    while position<=len(cards):
        if cards[position]==query:

            return position
        position+=1
    return -1

tests=[{'input':{'cards':[13,11,10,7,4,3,1,0],'query':7},'output':3},{'input':{'cards':[9,8,7,6,5],'query':7},'output':2}]
for test in tests:
  result=locate_card(test['input']['cards'],test['input']['query'])
  if result==test['output']:
      print("Test Case is Successful")
  else:
      print("Test case Got Erros")
