# Generated by Django 5.0.6 on 2024-05-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
