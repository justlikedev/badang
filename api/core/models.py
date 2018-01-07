#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from enum import Enum, EnumItem

class Person(User):
    
    class Type(Enum):
        Player = EnumItem(_('Player'))
        Administrator = EnumItem(_('Administrator'))
        Teacher = EnumItem(_('Teacher'))

    class Gender(Enum):
        Female = EnumItem(_('Female'))
        Male = EnumItem(_('Male'))        

    photo = models.FileField(upload_to='uploads/users/photos/')
    person_type = models.CharField(max_length=1, choices=Type.to_tuples(), null=False)
    gender = models.CharField(max_length=1, choices=Gender.to_tuples(), null=False)    

    class Meta:
        verbose_name = _(u'Person')
        verbose_name_plural = _(u'Persons')

    def __unicode__(self):
        return u'Person - {0} {1}'.format(super.self.first_name, super.self.last_name)


class Player(Person):
    user = models.OneToOneField(Person, related_name='person_player')
    level = models.IntegerField(default=1, null=False)
    experience = models.IntegerField(default=1, null=False)
    friends = models.ManyToManyField(Person, related_name='friends_list')
    credits_quantity = models.IntegerField(default=10)

    class Meta:
        verbose_name = _(u'Player')
        verbose_name_plural = _(u'Players')

    def __unicode__(self):
        return u'Player - {0} {1}'.format(super.self.first_name, super.self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=254, null=False)
    description = models.CharField(max_length=254, null=True)

    class Meta:
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        return u'Category - {0}'.format(self.name)


class Question(models.Model):
    title = models.CharField(max_length=254, null=False)
    slug = models.CharField(max_length=254, null=False)
    answer = models.CharField(max_length=254, null=False)
    sound = models.FileField(upload_to='uploads/questions/sounds/')
    category = models.OneToOneField(Category, related_name='question_category')
    count = models.IntegerField(default=0)
    success = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)

    class Meta:
        verbose_name = _(u'Question')
        verbose_name_plural = _(u'Questions')

    def __unicode__(self):
        return u'Question - {0}'.format(self.title)


class PlayerQuestion(models.Model):
    player = models.ForeignKey(Player, related_name='player_questions')
    question = models.ForeignKey(Question, related_name='player_questions')
    readed = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)

    class Meta:
        verbose_name = _(u'Player Question')
        verbose_name_plural = _(u'Player Questions')


class Duel(models.Model):
    challenger = models.OneToOneField(Player, related_name='player_duel_challenger')
    guest = models.OneToOneField(Player, related_name='player_duel_guest')
    occurrence_date = models.DateTimeField(auto_now_add=True)
    winner = models.OneToOneField(Player, related_name='player_winner')
    
    class Meta:
        verbose_name = _(u'Duel')
        verbose_name_plural = _(u'Duels')
