from django.contrib import admin
from .models import Team, User, Category, Robot, Judge, Match

admin.site.register(Team)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Robot)
admin.site.register(Judge)
admin.site.register(Match)
