import math

def get_peri(radius = 5.0) :
    return math.pi * 2 * radius

if __name__ == "__main__" :
    print("get_peri() = ", get_peri())
    print("get_peri(4.0) = ", get_peri(4.0))