
    
st_grade=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    st_grade.append([name,score])
    
st_grade.sort(key=lambda x:(x[1],x[0]))
second=sorted(set(score for name,score in st_grade))[1]   
    
for name,grade in st_grade:
    if grade==second:
        print(name)
        
        
        
