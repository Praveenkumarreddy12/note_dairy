# Generated by Django 4.2.7 on 2024-08-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0005_alter_mypage_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypage',
            name='uid',
            field=models.CharField(max_length=40, null=True),
        ),
    ]