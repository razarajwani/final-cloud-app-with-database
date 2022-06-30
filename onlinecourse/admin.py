from secrets import choice
from django.contrib import admin
# <HINT> Import any new Models here
from .models import Choice, Course, Lesson, Instructor, Learner, Question

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']



class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

# <HINT> Register Question and Choice models here


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade')
    list_filter = ['question_text']
    search_fields = ['question_text']

class ChoiseAdmin(admin.ModelAdmin):
    list_display = ['choice_text','is_correct']
    list_filter = ['choice_text']
    search_fields = ['choice_text']



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiseAdmin)
