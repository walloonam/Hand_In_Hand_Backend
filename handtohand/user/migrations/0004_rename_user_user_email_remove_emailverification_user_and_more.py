# Generated by Django 4.2.3 on 2023-08-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_emailverification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='emailverification',
            name='user',
        ),
        migrations.AddField(
            model_name='emailverification',
            name='email',
            field=models.EmailField(default=2, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
