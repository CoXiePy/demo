# Generated by Django 3.2 on 2022-07-31 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('praise', models.IntegerField(default=0, verbose_name='点赞量')),
                ('reading', models.IntegerField(default=0, verbose_name='阅读量')),
                ('comments', models.IntegerField(default=0, verbose_name='评论量')),
                ('acticle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_comment', to='blog.article')),
            ],
            options={
                'verbose_name': '博客互动表',
                'verbose_name_plural': '博客互动表',
                'db_table': 'b_comment',
            },
        ),
    ]
