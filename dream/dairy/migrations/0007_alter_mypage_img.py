# Generated by Django 4.2.7 on 2024-08-31 10:24

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0006_alter_mypage_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypage',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=django.forms.fields.FilePathField),
        ),
    ]
