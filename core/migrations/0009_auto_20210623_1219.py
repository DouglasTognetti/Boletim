# Generated by Django 3.2.4 on 2021-06-23 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210623_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado',
            name='aprovado',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='notaFinal',
        ),
    ]
