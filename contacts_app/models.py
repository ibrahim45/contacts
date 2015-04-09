from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=75)
    number=models.CharField(max_length=13)
    
    def __unicode__(self): 
        
        return u'%s' %(self.name)
        
        
    
