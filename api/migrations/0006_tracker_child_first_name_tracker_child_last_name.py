# Generated by Django 4.0.2 on 2022-02-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_name_tracker_child_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='child_first_name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracker',
            name='child_last_name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]