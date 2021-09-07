from django.contrib import admin
from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug", )  #faqat slugni uqiydi             # adminda uzgartirish kiritish  
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")     


class  AddressAdmin(admin.ModelAdmin):
    list_display = ("city","street",)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)