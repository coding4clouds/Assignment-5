list=[1,2,3,4,5,6,7,8,9,10]
print('Original list:',list)
elt=list[:5]
print('Extracted first five elements: ',elt)
a=elt.copy()
a.reverse()
print('Reversed extracted elements:',a)