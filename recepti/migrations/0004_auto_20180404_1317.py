# Generated by Django 2.0.3 on 2018-04-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0003_jela_svidja_mi_se'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jela',
            name='nacin_pripreme',
            field=models.TextField(),
        ),
    ]
