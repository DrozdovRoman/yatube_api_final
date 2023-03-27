# Generated by Django 3.2 on 2023-03-27 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.group'),
        ),
    ]