# Generated by Django 4.1.2 on 2022-10-18 20:33

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=60)),
                ('campus_ID', models.IntegerField(blank=True, default='')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]