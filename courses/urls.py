from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    # path('test-session/', views.test_session, name='test-session'),
    # path('test-delete/', views.test_delete, name='test-delete'),

    path('course/<course_id>', views.Courses.as_view(), name='course'),

    path('favourites/<course_id>', views.Favourites.as_view(), name='favourites'),
    path('bookmarked/', views.Bookmarked.as_view(), name='bookmarked'),


    path('enroll-course/<course_id>', views.Enroll.as_view(), name='enroll'),
    path('enrolled/', views.Enrolled.as_view(), name='enrolled'),

    path('test/', views.Test.as_view(), name='test'),
    path('test-courses/<video_id_>', views.TestCourses.as_view(), name='test_courses')

]
