# Generated by Django 3.2 on 2022-08-15 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='acticle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_comment', to='blog.article'),
        ),
    ]
