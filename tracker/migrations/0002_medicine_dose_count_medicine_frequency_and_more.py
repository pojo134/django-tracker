# Generated by Django 4.2.9 on 2025-03-26 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dose_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='medicine',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily', max_length=10),
        ),
        migrations.AlterField(
            model_name='medicinelog',
            name='taken',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
