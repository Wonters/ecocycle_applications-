# Generated by Django 2.2.3 on 2019-07-17 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tierlieu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statu',
            old_name='competance',
            new_name='comp',
        ),
    ]
