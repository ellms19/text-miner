from django.http import request
from apps.mine.models import Classroom

app_superuser = 'textminersmtp@gmail.com'


def main_classrooms(request):
    classrooms = Classroom.objects.filter(owner__email=app_superuser)
    return {'main_classrooms': classrooms}