# Generated by Django 4.1.2 on 2022-10-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='static/images/projects/default.png', null=True, upload_to='static/images/projects'),
        ),
    ]
