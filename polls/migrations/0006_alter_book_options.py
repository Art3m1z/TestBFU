# Generated by Django 4.1.7 on 2023-02-18 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20230218_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author', 'book_name']},
        ),
    ]
