# Generated by Django 2.0.4 on 2018-06-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180524_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanism',
            name='rating_dislikes',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='mechanism',
            name='rating_likes',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False),
        ),
    ]