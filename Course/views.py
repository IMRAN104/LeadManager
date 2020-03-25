from django.shortcuts import render

from .models import Course, Step


# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Courses/course_list.html', {'courses': courses})


def course_details(request):
    course = Course.objects.get(pk=pk)
    return render(request, 'Courses/course_details.html', {'course': course})
