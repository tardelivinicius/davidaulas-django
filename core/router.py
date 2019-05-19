from rest_framework import routers
from student.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
