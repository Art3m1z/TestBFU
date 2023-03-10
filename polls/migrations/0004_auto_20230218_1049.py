# Generated by Django 2.2.12 on 2023-02-18 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_comment_date_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='first_name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='last_name',
        ),
        migrations.AddField(
            model_name='book',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
