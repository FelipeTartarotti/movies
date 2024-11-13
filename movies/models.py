# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da linguagem")

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da categoria")

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título do filme")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    languages = models.ManyToManyField(Language, verbose_name="Linguagens")

    def __str__(self):
        return str(self.title)
