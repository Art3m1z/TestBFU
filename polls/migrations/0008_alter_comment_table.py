# Generated by Django 4.1.7 on 2023-02-19 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_book_options_comment_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]
