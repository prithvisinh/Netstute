# Generated by Django 3.0.7 on 2020-11-10 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='timetableStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timetable', models.FileField(upload_to='time_table/student/')),
                ('Field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Field')),
            ],
        ),
        migrations.CreateModel(
            name='timetableHOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timetable', models.FileField(upload_to='time_table/Faculty/')),
                ('Enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Enrollment')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Field')),
            ],
        ),
    ]
