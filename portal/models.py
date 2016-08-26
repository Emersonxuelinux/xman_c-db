from django.db import models
from datetime import datetime

# Create your models here.

class Host(models.Model):
	name = models.CharField(max_length = 45)
	ip = models.CharField(max_length = 30)
	cname = models.CharField(max_length = 45)
	idc_id = models.IntegerField()
	role = models.CharField(max_length = 10)
	rack = models.CharField(max_length = 30)
	assert_num = models.CharField(max_length = 30)	
	u_phone = models.IntegerField()
	u_id = models.IntegerField()
	update_time = models.DateTimeField(default=datetime.now)
	rep_info = models.CharField(max_length = 45)
	post_time = models.IntegerField()
	status = models.IntegerField(default='0')
	modelNum = models.CharField(max_length = 45,default='0000-0000')
	

	def __str__(self):
		return self.name

class Idc(models.Model):
        name = models.CharField(max_length = 30)
        company = models.CharField(max_length = 30)
        update_time = models.DateTimeField(default=datetime.now)

#        def __str__(self):
#                return self.name

class Maintance(models.Model):
        title = models.CharField(max_length = 30)
        msg = models.CharField(max_length = 300)
        ip = models.CharField(max_length = 30)
        idc_id = models.IntegerField()
        update_time = models.DateTimeField(default=datetime.now)

        def __str__(self):
                return self.title
class saltTask(models.Model):
	title = models.CharField(max_length = 45)
	cmd = models.CharField(max_length = 100)
	u_id = models.IntegerField()
	host_id = models.IntegerField()
	update_time = models.DateTimeField(default=datetime.now)

