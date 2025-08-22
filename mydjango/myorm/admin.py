from django.contrib import admin

from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", )
    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", )
    
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("level", )
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", )
    
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", )


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Course, CourseAdmin)
