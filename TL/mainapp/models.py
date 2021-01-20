from django.db import models

class Order(models.Model):

    SCHOOL = 'school'
    COLLEGE = 'college'
    UNIVERSITY = 'university'
    MASTERS = 'masters'
    PHD = 'phd'

    words = models.CharField(max_length=32)
    level = models.CharField(max_length=32)

