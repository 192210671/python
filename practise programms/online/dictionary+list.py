#dictionary + list
keys=['Eswar','Sriram','Vamsi']
values=['python','java','javascript']

#merging to list

data=dict(zip(keys,values))
data
data['Eswar']
#adding new key to dictionary
data['murali']='sql'
data
#deleting the key
del data['Eswar']
data
