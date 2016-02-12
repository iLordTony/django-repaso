from django.contrib import admin
from library.models import Editor, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)
    search_fields = ('name', 'surname',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'editor', 'publication_date',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'editor',)  # Fields that can be edited
    filter_horizontal = ('authors',)
    raw_id_fields = ('editor',)

admin.site.register(Editor)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)