

List=[1,2,3,4,5,6,7,8,9,10,11]

for i in range(len(List)):
    List[i]=input("Enter a name:").strip()

name=input("Enter a name to be searched:").strip()
if name in List:
    position = List.index(name)
    print("Position of name:", position)
else:
    print("Name not found.")



#eqSize = 0
#for j in range(len(List)):
#    if name == List[j]:
#        position = j
#    else:
#        eqSize += 1
#if eqSize == len(List):
#    print("Name not found.")
#else:
#    print("Position of name: ", position)




#if List.count(name) == 0:
#    print("Name not found.")
#else:
#    for i in range(len(List)):
#        if name==List[i]:
#            print("Position of name: ", i)
    