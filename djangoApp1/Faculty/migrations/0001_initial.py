# Generated by Django 2.1.5 on 2019-02-01 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyid', models.AutoField(primary_key=True, serialize=False)),
                ('facultyname', models.CharField(max_length=100)),
                ('facultyaddress', models.CharField(max_length=100)),
                ('facultymobileno', models.IntegerField()),
                ('facultyemail', models.EmailField(max_length=254)),
                ('facultysalary', models.IntegerField()),
                ('fusername', models.CharField(max_length=10)),
                ('passwd', models.CharField(max_length=6)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Courses')),
            ],
        ),
    ]
