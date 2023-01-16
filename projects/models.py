from django.db import models  
class Projects(models.Model):  
    eid = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)  
    image = models.CharField(max_length=100)   
    url = models.CharField(max_length=100) 
    techno = models.CharField(max_length=100) 

    def __str__(self):
        return "%s " %(self.name) 
    class Meta:  
        db_table = "projects"  