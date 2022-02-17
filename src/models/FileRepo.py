from asyncore import write
import Point as pt

class FileRepo:
    """FileRepo class : a class that deal with saving the data into a CSV file"""
    def __init__(self, points:list):
        self.points = points
        self.importString = ""
        
    def ToString(self,point):   
        return("{0};{1};{2}".format(point.getX(),point.getY(), point.getTime()))

    def export2CSV(self):
        """the actual export function : opens the file "TrackingDataSheet.CSV" ( or create it if it does not exist ) and stores the data in this file"""
        for i in self.points:
            self.importString += self.ToString(i)+"\n"
        
        with open('TrackingDataSheet.CSV', 'a') as Data:
            Data.write(self.importString)

if __name__ == "__main__":
    pointlist = [pt.Point(1,2,30),pt.Point(10,20,60), pt.Point(100,200,600)]

    Export = FileRepo(pointlist)
    Export.export2CSV()