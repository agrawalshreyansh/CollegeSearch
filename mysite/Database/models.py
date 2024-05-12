from django.db import models

# Create your models here.
class JossaCollegeData (models.Model):
    CollegeID=models.IntegerField()
    CollegeName = models.CharField(max_length=100)
    CollegeDescription= models.CharField(max_length=500)
    OpeningRank=models.CharField(max_length=10)
    ClosingRank = models.CharField(max_length=10)
    HeighestPackage=models.CharField(max_length=20)
    AveragePackage = models.CharField(max_length=20)
    CampusFile = models.FileField()


class JossaCollegeBranchData (models.Model):
    CollegeID = models.IntegerField()
    BranchName = models.CharField(max_length=100)
    BranchOpeningRank = models.CharField(max_length=100)
    BranchClosingRank = models.CharField(max_length=100)