# Generated by Django 3.2.5 on 2021-11-18 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0004_remove_record_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record', to=settings.AUTH_USER_MODEL),
        ),
    ]
