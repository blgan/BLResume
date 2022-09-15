from django.contrib import admin
from .models import About, Experience, Education, Skill, Language, Award

# Register your models here.

admin.site.register(About),
admin.site.register(Experience),
admin.site.register(Education),
admin.site.register(Skill),
admin.site.register(Language),
admin.site.register(Award),