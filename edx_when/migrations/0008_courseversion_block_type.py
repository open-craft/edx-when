# Generated by Django 3.2.6 on 2021-09-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_when', '0007_meta_tweaks'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentdate',
            name='block_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddIndex(
            model_name='contentdate',
            index=models.Index(fields=['course_id', 'block_type'], name='edx_when_course_block_type_idx'),
        ),
    ]
