# Generated by Django 2.2.2 on 2019-06-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190627_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.CharField(default='slug', max_length=255),
            preserve_default=False,
        ),
    ]