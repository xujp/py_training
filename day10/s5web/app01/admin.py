from django.contrib import admin

# Register your models here.
from app01.models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    search_fields=('title',)


class bbsAdmin(admin.ModelAdmin):
	list_display = ('title','author','view_count','comment_count','publish_date')
	
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(bbs,bbsAdmin)
