from django.db import models  
class Projects(models.Model):  
    id = models.AutoField(primary_key=True,auto_created = True) 
    name = models.CharField(max_length=100)  
    # description = models.CharField(max_length=200)  
    image = models.FileField(null="True",blank="True",upload_to="images/")   
    url = models.URLField(max_length=100) 
    techno = models.CharField(max_length=100) 
    status = models.CharField(max_length=20) 

    def __str__(self):
        return "%s " %(self.name) 
    class Meta:  
        db_table = "projects"
        verbose_name = "project"
        verbose_name_plural = "projects"