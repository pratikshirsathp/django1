# Generated by Django 3.1 on 2020-08-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emails',
            new_name='email',
        ),
    ]