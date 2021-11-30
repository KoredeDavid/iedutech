import json
import os

import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View

from .forms import NewsLetterForm
from .models import Course


def test(request):
    return render(request, 'test.html', )


class Index(View):
    def get(self, request):
        pass
    #     global res
    #     form = NewsLetterForm()
    #     categories = list(Category.objects.all())
    #     favourites = request.session.get('favourites', [])
    #     print(favourites)
    #     context = {
    #         'categories': categories,
    #         'favourites': favourites,
    #         'form': form
    #     }
    #     return render(request, 'index.html', context)
    #
    # def post(self, request):
    #     form = NewsLetterForm(request.POST)
    #     categories = list(Category.objects.all())
    #     favourites = request.session.get('favourites', [])
    #     context = {
    #         'categories': categories,
    #         'favourites': favourites,
    #         'form': form
    #     }
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         form.save()
    #         subject = 'KoredeDavid from EduTech'
    #         message = f'Hi {name.capitalize()}, I just want to say thank you for signing up for our News Letter. We ' \
    #                   f'are committed to serving you with  our latest gist '
    #         if os.environ.get('DJANGO_ENV', '') == 'production':
    #             email_from = os.environ.get('EMAIL_HOST_USER', '')
    #         else:
    #             email_from = 'test@email.com'
    #         recipient_list = [email, ]
    #         send_mail(subject, message, email_from, recipient_list, )
    #         messages.success(request, f'Thank you {name.capitalize()}')
    #         return redirect('/#news')
    #     return render(request, 'index.html', context)


class Courses(View):
    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise Http404('This course does not exist')

        enrolled_courses = request.session.get('enrolled_courses', [])

        context = {
            'course': course,
            'category': str(course.category),
            'enrolled_courses': enrolled_courses
        }
        return render(request, 'course.html', context)


class Enroll(View):
    def post(self, request, course_id):
        enrolled_courses = request.session.get('enrolled_courses', [])
        if course_id not in enrolled_courses:
            enrolled_courses.append(course_id)
            request.session['enrolled_courses'] = enrolled_courses
            request.session.modified = True
            print('Added', request.session.get('enrolled_courses', []))
        else:
            enrolled_courses.remove(course_id)
            request.session['enrolled_courses'] = enrolled_courses
            request.session.modified = True
            print('Removed', request.session.get('enrolled_courses', []))

        return HttpResponse('Success')


class Enrolled(View):
    def get(self, request):
        enrolled_courses = request.session.get('enrolled_courses', [])

        context = {
            'enrolled_courses': enrolled_courses
        }
        return render(request, 'enrolled.html', context)


class Bookmarked(View):
    def get(self, request):
        bookmarked = request.session.get('favourites', [])

        context = {
            'bookmarked': bookmarked
        }
        return render(request, 'bookmarked.html', context)


class Favourites(View):
    def post(self, request, course_id):
        favourites = request.session.get('favourites', [])
        course_id = int(course_id)
        if course_id not in favourites:
            favourites.append(course_id)
            request.session['favourites'] = favourites
            request.session.modified = True
            print('Added', request.session.get('favourites', []))
        else:
            favourites.remove(course_id)
            request.session['favourites'] = favourites
            request.session.modified = True
            print('Removed', request.session.get('favourites', []))

        return HttpResponse('Success')


class Test(View):
    def get(self, request):
        youtube_courses = Course.objects.all()

        context = {
            'courses': youtube_courses
        }
        return render(request, 'test.html', context=context)


class TestCourses(View):
    def get(self, request, video_id_):
        youtube_course = Course.objects.get(video_id=video_id_)
        youtube_api_key = "AIzaSyAPImkfCCrwHl5sjC_Zg-U0BE6Qvh35iW8"
        video_id = youtube_course.video_id
        channel_id = youtube_course.channel_id
        url = "https://www.googleapis.com/youtube/v3"

        # Comments EndPoint
        comments_url = f"{url}/commentThreads?part=snippet&videoId={video_id}&key={youtube_api_key}&textFormat=plainText&maxResults=5&order=relevance"
        comments_response = requests.get(comments_url)
        comments_content = comments_response.content.decode("utf8")
        comments_js = json.loads(comments_content)
        comments = comments_js['items']

        # Video Details EndPoint
        video_details_url = f"{url}/videos?part=snippet%2CcontentDetails%2Cstatistics%2CtopicDetails&id={video_id}&key={youtube_api_key}"
        video_details_response = requests.get(video_details_url)
        video_details_content = video_details_response.content.decode("utf8")
        video_details_js = json.loads(video_details_content)
        video_details = [video_details_js['items'][0]['snippet'], video_details_js['items'][0]['statistics']]

        # Channel Details EndPoint
        channel_details_url = f"{url}/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channel_id}&key={youtube_api_key}"
        channel_details_response = requests.get(channel_details_url)
        channel_details_content = channel_details_response.content.decode("utf8")
        channel_details_js = json.loads(channel_details_content)
        channel_details = [channel_details_js['items'][0]['snippet'], channel_details_js['items'][0]['statistics']]

        context = {
            "comments": comments,
            "video_details": video_details,
            "channel_details": channel_details,
            "video_id": video_id,
            "channel_id": channel_id,
            "youtube_course": youtube_course
        }
        return render(request, 'test_courses.html', context)
