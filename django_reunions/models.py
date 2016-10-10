# -*- coding:utf-8 -*-
from datetime import date

from django.db import models
from django.utils import timezone

# Create your models here.
class Institution(models.Model):
    name = models.CharField('Organisme', max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField('Nom', max_length=50)
    last_name = models.CharField('Prénom', max_length=50)
    function = models.CharField('Fonction', max_length=50, blank=True)
    email = models.EmailField('Adresse E-Mail', blank=True)
    phone = models.CharField('Téléphone', max_length=30, blank=True)
    mobile = models.CharField('GSM', max_length=30, blank=True)
    institution = models.ForeignKey(Institution, blank=True, null=True)

    class Meta():
        verbose_name = "Personne"

    def __str__(self):
        if self.function:
                title = " - " + self.function
        else:
                title = ""
        if self.institution:
                institution = " (%s)" % self.institution
        else:
                institution = ""
        return "%s %s%s%s" % (self.first_name, self.last_name, title, institution)


class Reunion(models.Model):
    place = models.CharField('Lieu',max_length=100)
    date = models.DateField('Date de réunion', default=date.today)
    time_start = models.TimeField('Heure de debut',max_length=20, blank=True, null=True)
    time_end = models.TimeField('Heure de fin',max_length=20, blank=True, null=True)
    subject = models.CharField('Ordre du jour',max_length=200)
    participants = models.ManyToManyField(Person)
    pv = models.TextField('Procès verbal de réunion')

    class Meta():
        verbose_name = "Réunion"

    def __str__(self):
        return self.subject
