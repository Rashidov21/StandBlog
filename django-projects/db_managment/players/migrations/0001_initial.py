# Generated by Django 4.1.5 on 2023-04-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='club_logos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birthday', models.DateTimeField(blank=True)),
                ('image', models.ImageField(upload_to='players/%Y/%m/%d')),
                ('height', models.FloatField(blank=True)),
                ('weight', models.FloatField(blank=True)),
                ('country', models.CharField(blank=True, max_length=150)),
                ('position', models.CharField(blank=True, choices=[('gk', 'Goalkeeper'), ('df', 'Deffender'), ('md', 'Middle Deffender'), ('fw', 'Forward'), ('st', 'Striker')], max_length=50)),
                ('current_price', models.FloatField(blank=True, default=0)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='players', to='players.club')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='players/%Y/%m/%d')),
                ('player', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_images', to='players.player')),
            ],
            options={
                'verbose_name': 'Player rasmlari',
                'verbose_name_plural': 'Player rasmlari',
            },
        ),
    ]
