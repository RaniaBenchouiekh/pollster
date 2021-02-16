from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


''' TabularInline makes it possible to view the choices
    of the question, under the question itself
'''


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # This means how many extra fields are needed


''' The 'None' field is supposed to be a name, but we don't need that
    The second parameter of fieldset is a dictionary
'''


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# The possibility to add Questions and Choices from the backend (browser)
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
