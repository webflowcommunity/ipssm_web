# Generated by Django 4.1.5 on 2023-05-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_newsletter_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherachi',
            name='designation',
            field=models.CharField(default=1, max_length=50, verbose_name='Designation'),
            preserve_default=False,
        ),
    ]
