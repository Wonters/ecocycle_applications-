# Generated by Django 2.2.3 on 2019-07-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tierlieu', '0003_auto_20190718_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeadhesion',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]