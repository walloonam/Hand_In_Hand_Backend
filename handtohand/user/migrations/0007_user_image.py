# Generated by Django 4.2.3 on 2023-08-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_attendance_date_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='simple.png', null=True, upload_to='user/'),
        ),
    ]