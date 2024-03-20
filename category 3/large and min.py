li=[1,20,40,50,59,23,60]
k=len(li)
max=1
min=3

li=sorted(li)

m_max=li[-max]
m_min=li[min-1]


print("The {} largest element:{}".format(max,m_max))
print("The {} minimum element:{}".format(min,m_min))

print("Sum of {} and {} is  {}".format(m_max,m_min,m_max+m_min))

print("Difference  of {} and {} is  {}".format(m_max,m_min,m_max-m_min))

print("product of {} and {} is  {}".format(m_max,m_min,m_max*m_min))