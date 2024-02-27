from django.db import models
from .utils import from_cyrillic_to_eng


def defaults_url():
    return {'work': '', 'dou': ''}


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Name city'
        verbose_name_plural = 'Name cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Name language'
        verbose_name_plural = 'Name languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True, max_length=1000)
    title = models.CharField(max_length=500, verbose_name='title')
    company = models.CharField(max_length=500, verbose_name='company')
    description = models.TextField(verbose_name='description')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='city', related_name='vacancies')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
        ordering = ['-timestamp', ]

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.timestamp)


class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='city')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='language')
    url_data = models.JSONField(default=defaults_url)

    class Meta:
        unique_together = ('city', 'language')

