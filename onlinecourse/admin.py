from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Question, Instructor, Learner,Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
class ChoiceInline(admin.TabularInline):
    model = Choice
class ChoiceInline(admin.TabularInline):
    model = Choice


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
class ChoiceAdmin(admin.ModelAdmin):
    pass


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.register(Choice)
admin.register(Question)