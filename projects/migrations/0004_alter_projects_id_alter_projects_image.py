# Generated by Django 4.1.5 on 2023-01-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_options_rename_eid_projects_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FileField(upload_to='image'),
        ),
    ]