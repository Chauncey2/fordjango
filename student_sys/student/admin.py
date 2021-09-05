from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'phone', 'status', 'create_time')
    search_fields = ('name', 'profession')
    list_filter = ('sex', 'status', 'create_time')
    # fieldset 对应的是信息增加页显示的字段名
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'phone'),
                'status'
            )
        }),
    )


admin.site.register(Student, StudentAdmin)
