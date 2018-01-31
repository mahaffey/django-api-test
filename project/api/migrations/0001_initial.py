# Generated by Django 2.0 on 2017-12-11 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['role'],
            },
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='soldier',
            name='squad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soldiers', to='api.Squad'),
        ),
        migrations.AlterUniqueTogether(
            name='soldier',
            unique_together={('role', 'squad')},
        ),
    ]
