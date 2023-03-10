# Generated by Django 4.1.7 on 2023-03-14 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0011_alter_experience_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-pk'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-pk'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-pk'], 'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
    ]
