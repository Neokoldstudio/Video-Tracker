class Point:
    """point class : a class to store points data with getters and setters. ( include small log function )"""
    def __init__(self,x,y,t):
        self.__x = x
        self.__y = y
        self.__time = t

    def getX(self):
        """getter for the x value"""
        return self.__x

    def getY(self):
        """getter for the y value"""
        return self.__y

    def getTime(self):
        """getter for the y value"""
        return self.__time