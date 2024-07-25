def perimeter_of_rectangle(length,breadth):
    perimeter = 2*(length + breadth)
    return perimeter

def area_of_rectangle(length,breadth):
    area = length * breadth
    return area

len=20
brh=15
required_result1 = perimeter_of_rectangle(len,brh)
required_result2 = area_of_rectangle(len,brh)

print("Perimeter of rectangle is=",required_result1)
print("area of rectangle is=",required_result2)

