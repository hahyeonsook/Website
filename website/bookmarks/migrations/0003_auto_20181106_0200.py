# Generated by Django 2.1.3 on 2018-11-05 17:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0002_remove_bookmarks_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookmarks',
            new_name='Bookmark',
        ),
    ]