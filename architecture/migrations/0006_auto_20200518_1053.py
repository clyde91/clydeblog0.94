# Generated by Django 3.1 on 2020-05-18 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0005_architect_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='architecture.country'),
        ),
        migrations.AlterField(
            model_name='architect',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='architecture/img_architect'),
        ),
    ]
