# Generated by Django 5.1.3 on 2024-12-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFerre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
