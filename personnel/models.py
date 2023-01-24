from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Personnel(models.Model):
    # days since joined -> serializers
    # create_user?

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    title = models.CharField(max_length=30, blank=False)
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('d', 'Diverse'),
        ('x', 'None')
    )
    gender = models.CharField(max_length=10, choices=GENDER, blank=False, null=True)
    salary = models.IntegerField(blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        ordering = ('last_name', 'first_name')
