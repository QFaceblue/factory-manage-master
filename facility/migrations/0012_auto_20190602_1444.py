# Generated by Django 2.0 on 2019-06-02 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0011_auto_20190602_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repair',
            options={'ordering': ['-baoxiu_time']},
        ),
    ]
