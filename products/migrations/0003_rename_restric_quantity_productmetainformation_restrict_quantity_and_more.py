# Generated by Django 4.2.5 on 2024-01-10 07:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_uid_alter_productimage_uid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmetainformation',
            old_name='restric_quantity',
            new_name='restrict_quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c01a87f9-13c5-4b39-adc6-cfc884ff02e0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c01a87f9-13c5-4b39-adc6-cfc884ff02e0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productmetainformation',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c01a87f9-13c5-4b39-adc6-cfc884ff02e0'), editable=False, primary_key=True, serialize=False),
        ),
    ]
