from django.contrib import admin
from .models import Team, Category, Robot, Judge, Match, Profile

admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Robot)
admin.site.register(Judge)
admin.site.register(Match)
admin.site.register(Profile)
