from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Klub(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název klubu', help_text='Zadejte název klubu',
                             error_messages={'blank': 'Název klubu musí být vyplněn'})
    misto = models.CharField(max_length=30, verbose_name='Město (obec)', help_text='Zadejte jméno města nebo obce',
                             error_messages={'blank': 'Jméno města nebo obce musí být vyplněno'})
    zalozeni = models.IntegerField(blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2022)], verbose_name='Rok založení',
                                   help_text='Zadejte rok založení')
    logo = models.ImageField(blank=True, upload_to='loga', verbose_name='Logo klubu', help_text='Zadejte logo klubu')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Klub'
        verbose_name_plural = 'Kluby'

    def __str__(self):
        return f'{self.nazev}, {self.misto}'


class Cyklista(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno cyklisty',
                             error_messages={'blank': 'Jméno cyklisty musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení', help_text='Zadejte příjmení cyklisty',
                                error_messages={'blank': 'Příjmení cyklisty musí být vyplněno'})
    narozeni = models.DateField(blank=True, verbose_name='Datum narození', help_text='Zadejte datum narození')
    fotka = models.ImageField(blank=True, upload_to='fotky', verbose_name='Fotka cyklisty')
    kariera = models.TextField(blank=True, verbose_name='Kariéra')
    klub = models.ForeignKey('Klub', on_delete=models.CASCADE, verbose_name='Klub')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Cyklista'
        verbose_name_plural = 'Cyklisté'

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'
