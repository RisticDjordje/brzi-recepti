# Generated by Django 2.0.3 on 2018-04-16 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0009_auto_20180406_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jela',
            name='sastojci',
        ),
        migrations.AddField(
            model_name='jela',
            name='sastojci',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recepti.Sastojci'),
        ),
    ]
