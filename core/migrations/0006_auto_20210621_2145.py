# Generated by Django 3.2.4 on 2021-06-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_resultado_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resultado',
            name='notaFinal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
