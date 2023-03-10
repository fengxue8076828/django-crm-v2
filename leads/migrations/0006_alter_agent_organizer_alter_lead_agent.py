# Generated by Django 4.0.4 on 2023-01-03 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_user_is_agent_user_is_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='organizer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.organizer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
