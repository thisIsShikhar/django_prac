from django.db import models

class Entry(models.Model):
    date=models.DateField(null=True)
    emp_id=models.IntegerField(null=True)
    name=models.CharField(max_length=200, null=True)
    punchin=models.TimeField(null=True)
    punchout=models.TimeField(null=True)
    spent=models.TimeField(null=True)
    deficiency=models.TimeField(null=True)
    percentile=models.IntegerField(null=True)
    status=models.CharField(max_length=100,null=True)
    emotion=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


