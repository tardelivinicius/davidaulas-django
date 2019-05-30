from rest_framework import routers
from student.views import StudentViewSet
from courses.views import CourseViewSet, CourseDataViewSet
from roomclass.views import RoomClassViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'courses_hour', CourseDataViewSet, basename='courses_hour')
router.register(r'class', RoomClassViewSet, basename='class')
