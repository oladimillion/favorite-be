# Generated by Django 2.2.3 on 2019-07-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
