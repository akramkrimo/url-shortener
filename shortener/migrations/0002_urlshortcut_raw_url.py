# Generated by Django 2.2.3 on 2019-10-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortcut',
            name='raw_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
