# Generated by Django 4.2.9 on 2024-02-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0015_pattern_link_pattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='link_pattern',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs/'),
        ),
    ]