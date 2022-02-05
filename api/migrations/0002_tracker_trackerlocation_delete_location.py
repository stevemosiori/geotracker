# Generated by Django 4.0.2 on 2022-02-05 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('tracker_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'trackers',
            },
        ),
        migrations.CreateModel(
            name='TrackerLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tracker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tracker')),
            ],
            options={
                'db_table': 'tracker_locations',
            },
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
