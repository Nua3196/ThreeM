# Generated by Django 4.2.3 on 2023-08-04 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_alter_updates_when'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(default=django.utils.timezone.now)),
                ('how', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Updates',
        ),
    ]
