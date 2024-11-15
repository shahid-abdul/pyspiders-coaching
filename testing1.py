lst = [5+8j,'Abdul',5.5,30,10,2.0,1+2j,20,3.5,'Tharun']
# l1_int = []
# l2_float = []
# l3_complex = []
# l4_str = []
# for i in lst:
#     if isinstance(i,int):
#         l1_int.append(i)
#         l1_int.sort()
#     elif isinstance(i,float):
#         l2_float.append(i)
#         l2_float.sort()
#     elif isinstance(i,complex):
#         l3_complex.append(i)
#     else:
#         l4_str.append(i)

# print(lst)
# print(l1_int+l2_float+l3_complex+l4_str)
s=[i for i in lst if isinstance(i,int)]+[i for i in lst if isinstance(i,float)]+[i for i in lst if isinstance(i,complex)]+[i for i in lst if isinstance(i,str)]
print(s)

