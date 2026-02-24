# Same as the previous problem, but for a cube. The constructor should
# accept the length of a side as a parameter.

class Cube:
    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length
    
    def surfaceArea(self):
        return 6 * self.length**2
    
    def volume(self):
        return self.length**3
    

def main():
    l = float(input("Enter length: "))
    c = Cube(l)
    print("Volume: ", c.volume(), ", Area: ", c.surfaceArea())

main()