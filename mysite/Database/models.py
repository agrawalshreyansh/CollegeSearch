from django.db import models

# Create your models here.
class JossaCollegeData (models.Model):
    CollegeID = models.IntegerField()
    CollegeName = models.CharField(max_length=100)
    CollegeDescription = models.CharField(max_length=500,null=True)
    OpeningRank = models.CharField(max_length=10)
    ClosingRank = models.CharField(max_length=10)
    HeighestPackage = models.CharField(max_length=20 , null=True)
    AveragePackage = models.CharField(max_length=20 , null=True)
    MedianPackage = models.CharField(max_length=20 , null=True)
    CampusFile1 = models.CharField(null=True , max_length=100)
    CampusFile2 = models.CharField(null=True , max_length=100)
    CampusFile3 = models.CharField(null=True , max_length=100)
    CollegeWebsite = models.CharField(max_length=100,null=True)
    NirfRank = models.CharField(max_length=30 , null=True)
    TotalSat = models.CharField(max_length=10 ,null=True)
    TotalStudent = models.CharField(max_length=10 ,null=True)
    TotalPlaced = models.CharField(max_length=10,null=True)



class JossaCollegeBranchData (models.Model):
    CollegeID = models.IntegerField()
    BranchName = models.CharField(max_length=100)
    BranchOpeningRank = models.CharField(max_length=100)
    BranchClosingRank = models.CharField(max_length=100)
    BranchHeighestPackage = models.CharField(max_length=20, null=True)
    BranchAveragePackage = models.CharField(max_length=20 , null=True)
    BranchMedianPackage = models.CharField(max_length=20 , null=True)