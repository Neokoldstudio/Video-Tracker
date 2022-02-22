from ast import Compare
from pyexpat import model
from random import sample
import filecmp
import unittest
import sys
sys.path.append("../../../../")
from models.FileRepo import FileRepo
from models.Point import Point

class test_FileRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__fileSample = "sample.csv"
        self.__pointList = [Point(1,2,30),Point(10,20,60), Point(100,200,600)]
        self.__FileRepo = FileRepo()
        self.__toStringSample = "1;2;30"

    def tearDown(self):
        pass

    def test_ToString(self):
        self.assertTrue(self.__FileRepo.ToString(self.__pointList[0]) == self.__toStringSample)

    def test_exportToCSV(self):
        self.__FileRepo.exportToCSV(self.__pointList)
        self.assertTrue(filecmp.cmp("TrackingDataSheet.CSV", self.__fileSample, shallow=False))

if __name__ == '__main__':
    unittest.main(verbosity=2)