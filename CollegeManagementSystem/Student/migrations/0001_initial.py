# Generated by Django 2.1.5 on 2019-01-20 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Department', '0001_initial'),
        ('Semester', '0001_initial'),
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.AutoField(primary_key=True, serialize=False)),
                ('studname', models.CharField(max_length=50)),
                ('studaddress', models.CharField(max_length=100)),
                ('studmobileno', models.IntegerField()),
                ('studemail', models.EmailField(max_length=254)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Courses')),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Department.Department')),
                ('semid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Semester.Semester')),
            ],
        ),
    ]
