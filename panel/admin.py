from django.contrib import admin
from .models import Student, Book, Borrow, Transaction

# Register your models here.
admin.site.register(Student),
admin.site.register(Book),
admin.site.register(Borrow),
admin.site.register(Transaction),