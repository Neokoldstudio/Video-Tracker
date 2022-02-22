from asyncore import write
from models.Point import Point

class FileRepo:
    """FileRepo class : a class that deal with saving the data into a CSV file"""
    def __init__(self):
        self.importString = ""
        
    def ToString(self,point):   
        return("{0};{1};{2}".format(point.getX(),point.getY(), point.getTime()))

    def exportToCSV(self,points):
        """the actual export function : opens the file "TrackingDataSheet.CSV" ( or create it if it does not exist ) and stores the data in this file"""
        for i in points:
            self.importString += self.ToString(i)+"\n"
        
        with open('TrackingDataSheet.CSV', 'w') as Data:
            Data.write(self.importString)

if __name__ == "__main__":
    pointlist = [Point(1,2,30),Point(10,20,60), Point(100,200,600)]

    Export = FileRepo(pointlist)
    Export.exportToCSV()