from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 250)
    datetime =  models.DateTimeField()
    department_id = models.IntegerField()
    job_id = models.IntegerField()

    class Meta:
        db_table = "employee"

    def __str__(self) -> str:
        return 'Employee ID: ' + str(self.intID) + ' Name: ' + self.strName
    
class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length= 250)

    class Meta:
        db_table = "department"

    def __str__(self) -> str:
        return 'Department ID: ' + str(self.intID) + ' Name: ' + self.strDepartment
        
class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.CharField(max_length= 250)

    class Meta:
        db_table = "job"

    def __str__(self) -> str:
        return 'Job ID: ' + str(self.intID) + ' Name: ' + self.strJob