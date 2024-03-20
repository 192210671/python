

import pandas as pd
li=[1,1,1,2,2,3,3,3,3,4,4,5,5,6,7,7,8,]
li=sorted(li)
count=pd.Series(li).value_counts()
print("Elements counts")
print(count)
