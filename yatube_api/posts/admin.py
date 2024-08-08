from django.contrib import admin

from .models import Comment, Follow, Group, Post

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'image', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_display_links = ('text',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
