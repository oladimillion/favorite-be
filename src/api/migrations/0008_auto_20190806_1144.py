# Generated by Django 2.2.3 on 2019-08-06 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190801_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-created_date']},
        ),
    ]
