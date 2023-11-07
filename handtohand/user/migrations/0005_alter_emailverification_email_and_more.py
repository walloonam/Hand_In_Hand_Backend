# Generated by Django 4.2.3 on 2023-08-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_user_user_email_remove_emailverification_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='email',
            field=models.EmailField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
