# Generated by Django 4.0.2 on 2022-02-05 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_tracker_id_trackerlocation_tracker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='name',
            new_name='child_id',
        ),
    ]
