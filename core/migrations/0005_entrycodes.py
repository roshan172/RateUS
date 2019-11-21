# Generated by Django 2.2.6 on 2019-11-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_subject_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Entry Code')),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Entry Codes',
                'verbose_name_plural': 'Entry Codes',
            },
        ),
    ]
