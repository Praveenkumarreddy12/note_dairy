# Generated by Django 4.2.7 on 2024-07-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0002_remove_mypage_tid_alter_mypage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypage',
            name='uid',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
