# Generated by Django 5.0.4 on 2024-04-16 03:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booked_user',
            field=models.ManyToManyField(related_name='booked_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='organizer_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.event'),
        ),
    ]
