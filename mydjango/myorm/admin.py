from django.contrib import admin

from . import models


admin.site.register(models.Author)
admin.site.register(models.Post)
admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Student)
admin.site.register(models.Course)
