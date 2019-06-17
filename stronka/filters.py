from .models import *
import django_filters


class RobotsFilter(django_filters.FilterSet):
    class Meta:
        model = Robot
        fields = ['Name','CategoryID','Group','TeamID']
class MatchesFilter(django_filters.FilterSet):

    class Meta:
            model = Match
            fields = ['CategoryID','Group']
class RacesFilter(django_filters.FilterSet):
    class Meta:
            model = Race
            fields = ['CategoryID']
class CategoriesFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['Description']
