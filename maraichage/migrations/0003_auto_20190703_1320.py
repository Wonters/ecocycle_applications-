# Generated by Django 2.2.3 on 2019-07-03 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maraichage', '0002_legum1_legum2_testmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Legum1',
        ),
        migrations.DeleteModel(
            name='Legum2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]