# Generated by Django 4.2.9 on 2024-02-04 22:27

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0011_remove_pattern_featured_image_alter_pattern_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='media/'),
        ),
    ]