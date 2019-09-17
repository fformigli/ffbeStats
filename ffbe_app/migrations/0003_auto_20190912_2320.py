# Generated by Django 2.2.5 on 2019-09-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffbe_app', '0002_hero_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='gender',
            field=models.CharField(default='M', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='race',
            field=models.CharField(default='human', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='role',
            field=models.CharField(default='mage', max_length=40),
            preserve_default=False,
        ),
    ]