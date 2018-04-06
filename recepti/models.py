from django.db import models


class Sastojci(models.Model):                                                 # npr mrkva, kupus, krompir, banana...
    ime = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Sastojci"

    def __str__(self):
        return self.ime


class Kategorije(models.Model):                                               # dorucak, rucak, vecera, dezert
    ime = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.ime


class Jela(models.Model):
    ime = models.CharField(max_length=100)
    slika = models.FileField()
    kategorija = models.ManyToManyField(Kategorije)
    sastojci = models.ManyToManyField(Sastojci)
    sastojci_opis = models.TextField(null=True)
    nacin_pripreme = models.TextField()
    je_vegeterijansko = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Jela"

    def __str__(self):
        return self.ime

