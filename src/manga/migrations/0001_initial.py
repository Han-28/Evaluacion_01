# Generated by Django 3.2.25 on 2025-04-09 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('manga_id', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('cover_url', models.URLField()),
                ('status', models.CharField(choices=[('reading', 'Leyendo'), ('completed', 'Completado'), ('planned', 'Planeado')], max_length=20)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
