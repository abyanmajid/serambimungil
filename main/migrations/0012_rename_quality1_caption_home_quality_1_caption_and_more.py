# Generated by Django 4.1.3 on 2023-02-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_home_featured_product_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='quality1_caption',
            new_name='quality_1_caption',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='quality1_heading',
            new_name='quality_1_heading',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='quality2_caption',
            new_name='quality_2_caption',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='quality2_heading',
            new_name='quality_2_heading',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='quality3_caption',
            new_name='quality_3_caption',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='quality3_heading',
            new_name='quality_3_heading',
        ),
        migrations.AddField(
            model_name='home',
            name='product_2_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='home',
            name='product_3_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
