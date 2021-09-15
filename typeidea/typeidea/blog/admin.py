from django.contrib import admin
from .models import Post, Category, Tag
from django.urls import reverse
from django.utils.html import format_html


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'create_time')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        """
        自定义方法，实例化后的对象保存在 list_display ,就可以显示了
        """
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_dispaly_links = [CategoryOwnerFilter]
    list_filter = ['category', ]
    search_fields = ['title', 'category_name']
    actions_on_top = True,
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = [
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag'
    ]

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id))
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
