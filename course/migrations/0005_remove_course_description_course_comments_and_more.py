# Generated by Django 4.0.6 on 2022-08-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_synopsis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='course',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_content',
            field=models.TextField(default='Course content'),
            preserve_default=False,
        ),
    ]
