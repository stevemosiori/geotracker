# Generated by Django 4.0.2 on 2022-02-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tracker_trackerlocation_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotspotRegions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bounding_box', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=255)),
                ('reason_text', models.CharField(max_length=500)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'hotspot_regions',
            },
        ),
    ]
