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
    sastojci = models.TextField()
    nacin_pripreme = models.TextField()
    kategorija = models.ForeignKey(Kategorije, on_delete=models.CASCADE)
    je_vegeterijansko = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Jela"

    def __str__(self):
        return self.ime


class SastojciUJelu(models.Model):
    jelo = models.ForeignKey(Jela, on_delete=models.CASCADE)
    sastojak = models.ForeignKey(Sastojci, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sastojci u jelu"


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)