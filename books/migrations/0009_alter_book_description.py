# Generated by Django 5.0.6 on 2024-09-03 19:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_comment_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
