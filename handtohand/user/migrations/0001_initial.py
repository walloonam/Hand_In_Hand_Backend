# Generated by Django 4.2.3 on 2023-07-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('user', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('nickname', models.CharField(default='', max_length=10)),
                ('date_of_birth', models.DateTimeField(max_length=20)),
                ('address', models.CharField(max_length=1000)),
                ('point', models.IntegerField()),
                ('adopt_count', models.IntegerField()),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.area')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
