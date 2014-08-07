# -*- coding: utf-8 *-*
from django.contrib import admin
from apps.notification.models import Notification, NotificationType


# class regCategoria(admin.ModelAdmin):
#     list_display = ('name', 'estudio',)
#     list_filter = ('estudio',)


# class regCuenta(admin.ModelAdmin):
#     list_display = ('estudio',
#     'actor', 'causa', 'debe', 'haber', 'saldo', 'actual',)
#     search_fields = ('actor', 'causa',)
#     list_filter = ('estudio', 'actor', 'causa', 'actual',)


# admin.site.register(Categoria, regCategoria)
# admin.site.register(Cuenta, regCuenta)
admin.site.register(Notification)
admin.site.register(NotificationType)
