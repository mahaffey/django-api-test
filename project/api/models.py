from django.db import models


class Squad(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Soldier(models.Model):
    COMMANDER = 'Commander'
    GUNNER = 'Gunner'
    MARKSMAN = 'Marksman'
    GRUNT = 'Grunt'
    ROLE_CHOICES = (
        (COMMANDER, 'Commander'),
        (GUNNER, 'Gunner'),
        (MARKSMAN, 'Marksman'),
        (GRUNT, 'Grunt')
    )

    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES,
        default=GRUNT
        )
    squad = models.ForeignKey(
        Squad,
        related_name='soldiers',
        on_delete=models.CASCADE,
        blank=True,
        default=''
        )

    class Meta:
        unique_together = ('role', 'squad')
        ordering = ['role']

    def __str__(self):
        return '%s %s -- Current Squad: %s' % (self.role, self.name, self.squad.name)
