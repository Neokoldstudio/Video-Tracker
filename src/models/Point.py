class Point:
    """point class : a class to store points data with getters and setters. ( include small log function )"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        """getter for the x value"""
        return self.x

    def getY(self):
        """getter for the y value"""
        return self.y
    
    def setX(self, newX):
        """setter for the x value, take a float as input"""
        self.x = newX

    def setY(self, newY):
        """setter for the y value, take a float as input"""
        self.y = newY

    def Log(self):#optional
        """quirky and silly little log function"""
        print("({0}, {1})".format(self.x,self.y))
    

if __name__ == "__main__":
    test = Point(300,200)
    test.Log()
    print(test.getX(), test.getY())