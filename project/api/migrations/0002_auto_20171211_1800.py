# Generated by Django 2.0 on 2017-12-11 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='squad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soldiers', to='api.Squad'),
        ),
    ]