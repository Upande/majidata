from django.db import models

class ColumnLabel(models.Model):
	column_name = models.CharField(max_length=100, blank=True, null=True)
	column_label = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return "%s" % self.column_name