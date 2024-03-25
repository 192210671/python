
def locate_card(cards,query):
    low=0
    high=len(cards)-1
    print("CARDS:",cards)
    print("QUERY:",query)

    while low<=high:
        mid=(low+high)//2
        mid_number=cards[mid]
        if mid_number==query:
            print("POSITION:",mid)
            return mid
        elif mid_number<query:
            high=mid-1
        elif mid_number>query:
            low=mid+1
    return -1

tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
             {'input': {'cards': [9, 8, 7, 6, 5], 'query': 7}, 'output': 2},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [9,3,4,5,6,6], 'query': 7}, 'output': -1}]
for test in tests:
    result=locate_card(test['input']['cards'],test['input']['query'])
    if result==test['output']:
        print("TEST CASE IS SUCCESSFUL")
    else:
        print("TEST CASE IS NOT SUCCESSFUL")
