# Generated by Django 4.1.7 on 2023-03-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0003_shorterurl_visitas_alter_shorterurl_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorterurl',
            name='visitas',
            field=models.IntegerField(default=0),
        ),
    ]