# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     """Регистрация модели CustomUser в админ панели"""

#     fieldsets = (
#         (None, {'fields': ('phone', 'password')}),
#         ('Personal info', {'fields': ('name', 'surname')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login',)}),
#     )

#     list_display = ('name', 'surname',)

#     list_filter = ('name', 'surname',)

#     search_fields = ('name', 'surname',)

#     filter_horizontal = ()

#     ordering = ('id',)

#     add_fieldsets = (
#         ("User Details", {'fields': ('phone', 'name', 'surname', 'password1', 'password2')}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)
