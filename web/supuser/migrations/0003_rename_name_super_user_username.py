# Generated by Django 4.2 on 2023-05-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supuser', '0002_rename_user_super_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super_user',
            old_name='name',
            new_name='username',
        ),
    ]