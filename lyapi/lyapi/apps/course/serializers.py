from rest_framework import serializers

from . import models


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherModelSerializer(serializers.ModelSerializer):
    """课程列表的老师信息"""

    class Meta:
        model = models.Teacher
        # fields = ['id', 'name', 'title', 'signature']
        fields = ["id", "name", "role", "title", "signature", "brief", "image"]


# 获取课程的数据
class CourseModelSerializer(serializers.ModelSerializer):
    # teacher_name = serializers.CharField(source='teacher.name')  #获取外建关联属性数据，就这么玩，通过sourse='关联属性.字段名称'
    # teacher = TeacherModelSerializer()  #序列化器嵌套  ，注意1：序列化器对象名称必须是关联属性名称
    teacher = TeacherModelSerializer()  # 序列化器嵌套  ，注意2：当多嵌套一时，不需要加参数，但是一嵌套多时，需要加上many=True参数

    # 获取课时数据，考虑到需要多层序列化器嵌套，效率较差，嵌套起来也容易乱套，我们通过自定义方法来玩，在course模型类中写一个获取课时的方法
    class Meta:
        model = models.Course
        # fields = ['id', 'name', 'course_img', 'students' , 'lessons', 'pub_lessons', 'price', 'teacher','teacher_name']
        # 模型类中的无参方法可以直接写到fields中 get_lessons
        # fields = ['id', 'name', 'course_img', 'students', 'lessons', 'pub_lessons', 'price', 'teacher', 'get_lessons']
        # fields = ['id', 'name', 'course_img', 'students', 'lessons', 'pub_lessons', 'price', 'teacher']
        fields = ["id", "name", "course_img", 'discount_name', 'real_price', "students", "lessons", "pub_lessons",
                  "price", "teacher", 'join_brief', "brief",
                  "level_name", 'get_lessons']


# 获取课程的数据
class CourseRetrieveSerializer(serializers.ModelSerializer):
    teacher = TeacherModelSerializer()
    class Meta:
        model = models.Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", "brief",
                  "level_name", 'course_video', 'discount_name', 'real_price','activity_time']


# 获取课程章节数据
class CourseDetailModelSerializer(serializers.Serializer):
    teacher = TeacherModelSerializer()

    class Meta:
        model = models.Course
        #  获取choice属性参数的值,可以直接使用get_属性名称_display
        fields = ['id', 'name', 'course_img',  'activity_time','students', 'lessons', 'join_brief', 'brief', 'teacher', 'pub_lessons',
                  'price','teacher', 'level_name']


class LessonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseLesson
        fields = ['id', 'name', 'section_link', 'duration', 'free_trail', 'lesson']



# 获取章节数据的是图
class ChapterModelSerializer(serializers.ModelSerializer):
    coursesections = LessonModelSerializer(many=True)  # 注意：一套多的时候，属性名称为related_name的值

    class Meta:
        model = models.CourseChapter
        fields = ['id', 'chapter', 'name', 'coursesections']


# # 把原来的讲师序列化器增加几个字段
# class TeacherSerializer(serializers.ModelSerializer):
#     """课程列表的老师信息"""
#
#     class Meta:
#         model = Teacher
#         fields = ["id", "name", "role", "title", "signature", "brief", "image"]


# class CourseChapterSerializer(serializers.ModelSerializer):
#     coursesections = CourseModelSerializer(many=True)
#
#     class Meta:
#         model = models.CourseChapter
#         fields = ["chapter", "name", "summary", "coursesections"]


class CourseCDetailModelSerializer(serializers.Serializer):
    class Mate:
        model = models.Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher",
                  'level_name', "brief"]
