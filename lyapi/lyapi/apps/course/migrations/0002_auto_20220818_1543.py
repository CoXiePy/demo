# Generated by Django 3.2 on 2022-08-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='b_course',
        ),
        migrations.AlterModelTable(
            name='coursecategory',
            table='b_course_category',
        ),
        migrations.AlterModelTable(
            name='coursechapter',
            table='b_course_chapter',
        ),
        migrations.AlterModelTable(
            name='coursediscounttype',
            table='b_course_discount_type',
        ),
        migrations.AlterModelTable(
            name='courseexpire',
            table='b_course_expire',
        ),
        migrations.AlterModelTable(
            name='courselesson',
            table='b_course_lesson',
        ),
        migrations.AlterModelTable(
            name='coursepricediscount',
            table='b_course_price_dicount',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='b_teacher',
        ),
    ]
