# Generated by Django 2.0.3 on 2018-04-06 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0007_auto_20180405_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sastojciujelu',
            name='jelo',
        ),
        migrations.RemoveField(
            model_name='sastojciujelu',
            name='sastojak',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='jela',
            name='sastojci_opis',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='jela',
            name='sastojci',
        ),
        migrations.AddField(
            model_name='jela',
            name='sastojci',
            field=models.ManyToManyField(to='recepti.Sastojci'),
        ),
        migrations.DeleteModel(
            name='SastojciUJelu',
        ),
    ]
