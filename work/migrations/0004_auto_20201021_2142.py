# Generated by Django 3.0.4 on 2020-10-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20201021_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]