# Generated by Django 3.2 on 2022-07-29 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_tagofarticle_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagofarticle',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
    ]