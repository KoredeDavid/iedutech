from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    path('enroll-course/<video_id>', views.Enroll.as_view(), name='enroll'),
    path('enrolled/', views.Enrolled.as_view(), name='enrolled_courses'),

    path('course-details/<video_id_>', views.CourseDetails.as_view(), name='course_details'),
    path('course-tutorial/<video_id_>', views.CourseTutorial.as_view(), name='course_tutorial'),

    path('get-comments', views.GetComments.as_view(), name='get_comments')

]
