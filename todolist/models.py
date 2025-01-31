from django.db import models

class Day(models.Model):
    day = models.DateField()
    def __str__(self):
        return str(self.day)
class Todo(models.Model):
    selected_day = models.ForeignKey(Day,on_delete=models.CASCADE)
    assignments = models.CharField(max_length=100)
    is_done = models.BooleanField()
    def __str__(self):
        return self.assignments
