# Generated by Django 4.1.5 on 2023-01-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=200, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.URLField(max_length=100),
        ),
    ]