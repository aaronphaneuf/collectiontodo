# Generated by Django 4.1.3 on 2022-11-05 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_remove_achievement_status_alter_achievement_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='achievements', to='to_do.user'),
        ),
    ]
