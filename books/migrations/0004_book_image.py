# Generated by Django 5.0.6 on 2024-05-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='cover/', verbose_name='image'),
        ),
    ]
