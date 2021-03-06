# Generated by Django 2.1.5 on 2019-02-01 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('Semester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subcode', models.AutoField(primary_key=True, serialize=False)),
                ('subname', models.CharField(max_length=25)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Courses')),
                ('semid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Semester.Semester')),
            ],
        ),
    ]
