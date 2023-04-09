def rect_area(length, width):
    area = length * width
    return area


def rect_surface_area(length, width, height):

    # Compute the surface area using the "rect_area" function
    top_bottom_area = rect_area(length, width)
    front_back_area = rect_area(length, height)
    left_right_area = rect_area(width, height)
    surface_area = 2 * (top_bottom_area + front_back_area + left_right_area)
    return surface_area


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

surface_area = rect_surface_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)