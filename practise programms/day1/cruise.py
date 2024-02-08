def max_guests_on_cruise(T, E, L):
    events = []  


    for i in range(len(E)):
        events.append((E[i], 1))
        events.append((L[i], -1))

    
    events.sort(key=lambda x: (x[0], -x[1]))

    current_guests = 0
    max_guests = 0  

    
    for event in events:
        time, event_type = event
        current_guests += event_type
        max_guests = max(max_guests, current_guests)

    return max_guests


print(max_guests_on_cruise(-4, [1, 5, 9, 10], [0, 2, 3, 4]))  
print(max_guests_on_cruise(0, [10, 2, 3, 4], [1, 2, 3, 4])) 
print(max_guests_on_cruise(4, [12, 85, 100], [0, 2, 3]))
print(max_guests_on_cruise(5, [42, 0, 35, 12, 15], [1, 2, 1, 3, 4]))  
print(max_guests_on_cruise(1, [12], [10]))  
