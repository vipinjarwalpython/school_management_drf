# Generated by Django 4.2.4 on 2023-12-06 07:27

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
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Faculty')),
            ],
        ),
    ]
