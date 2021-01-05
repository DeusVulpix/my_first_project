from django.db import models


class Tasks(models.Model):
    title = models.CharField('Task', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

class fight_tab(models.Model):
    choice_is = models.TextField(default='')
    yours = models.CharField('yours', max_length=12)
    dont_be_late = models.TextField(blank=True,null=True)

class user_stats(models.Model):
    user_name = models.CharField('nickname', max_length=12, default='Your nickname')
    hp = models.FloatField(default=100)
    damage = models.FloatField(default=27)

