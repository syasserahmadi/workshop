from django.contrib import admin
from .models import cuts, colors, sizes, lines, amounts, jobs



class cuts_admin(admin.ModelAdmin):
    list_display = ('id', 'cut', 'customcode', 'weight', 'colortype', 'sizetype', 'cdate', 'edate', 'completed')


class sizes_admin(admin.ModelAdmin):
    list_display = ('id', 'size', 'amount', 'cut')


class colors_admin(admin.ModelAdmin):
    list_display = ('id', 'color', 'amount', 'size', 'cut', 'completed')


class lines_admin(admin.ModelAdmin):
    list_display = ('id', 'line', 'price', 'color', 'completed')


class amounts_admin(admin.ModelAdmin):
    list_display = ('id', 'cut', 'totalcolors', 'totalsizes', 'totallines')


class jobs_admin(admin.ModelAdmin):
    list_display = ('id', 'cut', 'line', 'color', 'user', 'completed')

admin.site.register(cuts, cuts_admin)
admin.site.register(colors, colors_admin)
admin.site.register(sizes, sizes_admin)
admin.site.register(lines, lines_admin)
admin.site.register(amounts, amounts_admin)
admin.site.register(jobs, jobs_admin)