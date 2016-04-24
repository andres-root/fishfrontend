from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.humanize.templatetags.humanize import naturaltime


@python_2_unicode_compatible
class Fish(models.Model):
    color_choices = (
        ('0', 'Dark/gray'),
        ('1', 'Red'),
    )
    status_choices = (
        ('0', 'Correct'),
        ('1', 'Incorrect'),
    )
    name = models.CharField(max_length=200, null=False, blank=False)
    color = models.CharField(max_length=2, choices=color_choices)
    size = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=status_choices, default='0')
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, naturaltime(self.date_created))
