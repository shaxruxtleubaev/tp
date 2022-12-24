from django.contrib import admin
from .models import Product, Rubric, Author

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

admin.site.register(Product, ProductAdmin)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Rubric, RubricAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_display_links = ('author',)
    search_fields = ('author',)

admin.site.register(Author, AuthorAdmin)