from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug", )  #faqat slugni uqiydi             # adminda uzgartirish kiritish  
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")     



# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)