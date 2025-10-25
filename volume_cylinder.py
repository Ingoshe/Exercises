import math

def volume_of_cylinder(radius, height):
    """
    Calculate the volume of a cylinder.

    Parameters:
    radius (float): The radius of the cylinder base.
    height (float): The height of the cylinder.

    Returns:
    float: The volume of the cylinder.
    """
    return math.pi * radius**2 * height

if __name__ == "__main__":
    # Example usage
    r = float(input("Enter the radius of the cylinder: "))
    h = float(input("Enter the height of the cylinder: "))
    volume = volume_of_cylinder(r, h)
    print(f"The volume of the cylinder is: {volume:.2f}")