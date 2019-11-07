#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    side1 = input("Enter length of side one:")
    side2 = input("Enter length of side two:")
    side3 = input("Enter length of side three:")
    side1t = float(side1)
    side2t = float(side2)
    side3t = float(side3)
    perimeter = side1t + side2t + side3t
    semi_perimeter = perimeter / 2
    l1 = semi_perimeter - side1t
    l2 = semi_perimeter - side2t
    l3 = semi_perimeter - side3t
    area1 =  semi_perimeter * l1 * l2 * l3
    area_fin = area1**.5
    print ("Area of a triangle with sides",side1t,side2t,side3t,"is",area_fin)