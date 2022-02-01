from django.contrib import admin
from testapp.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','status']
    list_filter=('status','author','publish','created')
    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
