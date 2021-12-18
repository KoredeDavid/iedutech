import json
import os

import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import NewsLetterForm
from .models import Course

youtube_api_key = "AIzaSyAPImkfCCrwHl5sjC_Zg-U0BE6Qvh35iW8"
url = "https://www.googleapis.com/youtube/v3"


# Comments EndPoint
def comments_url(video_id, max_=5, page_token=""):
    url_ = f"{url}/commentThreads?part=snippet&videoId={video_id}&key={youtube_api_key}&textFormat=plainText&maxResults={max_}&order=relevance&pageToken={page_token}"
    comments_response = requests.get(url_)
    comments_content = comments_response.content.decode("utf8")
    comments_js = json.loads(comments_content)
    comments = comments_js.get('items', [])
    next_page_token = comments_js.get('nextPageToken')
    return comments, next_page_token


# Video Details EndPoint
def video_details_url(video_id):
    url_ = f"{url}/videos?part=snippet%2CcontentDetails%2Cstatistics%2CtopicDetails&id={video_id}&key={youtube_api_key}"
    video_details_response = requests.get(url_)
    video_details_content = video_details_response.content.decode("utf8")
    video_details_js = json.loads(video_details_content)
    video_details = [video_details_js['items'][0]['snippet'], video_details_js['items'][0]['statistics']]
    return video_details


# Channel Details EndPoint
def channel_details_url(channel_id):
    url_ = f"{url}/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channel_id}&key={youtube_api_key}"
    channel_details_response = requests.get(url_)
    channel_details_content = channel_details_response.content.decode("utf8")
    channel_details_js = json.loads(channel_details_content)
    channel_details = [channel_details_js['items'][0]['snippet'], channel_details_js['items'][0]['statistics']]
    return channel_details


# class Index(View):
#     def get(self, request):
#         pass
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
    def get(self, request, video_id):
        try:
            course = Course.objects.get(id=video_id)
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
    def post(self, request, video_id):
        enrolled_courses = request.session.get('enrolled_courses', [])
        if video_id not in enrolled_courses:
            enrolled_courses.append(video_id)
            request.session['enrolled_courses'] = enrolled_courses
            request.session.modified = True
            print('Added', request.session.get('enrolled_courses', []))
        else:
            enrolled_courses.remove(video_id)
            request.session['enrolled_courses'] = enrolled_courses
            request.session.modified = True
            print('Removed', request.session.get('enrolled_courses', []))

        return JsonResponse({'success': video_id})


class Enrolled(View):
    def get(self, request):
        enrolled_courses = request.session.get('enrolled_courses', [])

        context = {
            'enrolled_courses': enrolled_courses
        }
        return render(request, 'enrolled.html', context)


class Home(View):
    def get(self, request):
        youtube_courses = Course.objects.all()

        context = {
            'courses': youtube_courses
        }
        return render(request, 'home.html', context=context)


class CourseDetails(View):
    def get(self, request, video_id_):
        youtube_course = get_object_or_404(Course, video_id=video_id_)
        video_id = youtube_course.video_id
        channel_id = youtube_course.channel_id
        enrolled_courses = request.session.get('enrolled_courses', [])

        # Comments EndPoint
        comments, next_page_token = comments_url(video_id)

        # Video Details EndPoint
        video_details = video_details_url(video_id)

        # Channel Details EndPoint
        channel_details = channel_details_url(channel_id)

        context = {
            "comments": comments,
            "video_details": video_details,
            "channel_details": channel_details,
            "video_id": video_id,
            "channel_id": channel_id,
            "youtube_course": youtube_course,
            "enrolled_courses": enrolled_courses,
        }
        return render(request, 'course_details.html', context)


class CourseTutorial(View):
    def get(self, request, video_id_):
        youtube_course = get_object_or_404(Course, video_id=video_id_)
        enrolled_courses = request.session.get('enrolled_courses', [])
        if video_id_ not in enrolled_courses:
            raise Http404()
        video_id = youtube_course.video_id
        channel_id = youtube_course.channel_id

        # Comments EndPoint
        comments, next_page_token = comments_url(video_id)

        # Video Details EndPoint
        video_details = video_details_url(video_id)

        # Channel Details EndPoint
        channel_details = channel_details_url(channel_id)

        context = {
            "comments": comments,
            "next_page_token": next_page_token,
            "video_details": video_details,
            "channel_details": channel_details,
            "video_id": video_id,
            "channel_id": channel_id,
            "youtube_course": youtube_course,
        }
        return render(request, 'course_tutorial.html', context)


class GetComments(View):
    def post(self, request):
        video_id_ = request.POST.get('video_id')
        next_page_token_ = request.POST.get('next_page_token')
        youtube_course = get_object_or_404(Course, video_id=video_id_)
        video_id = youtube_course.video_id
        # channel_id = youtube_course.channel_id

        # Comments EndPoint
        comments, next_page_token = comments_url(video_id, 10, next_page_token_)

        # 'comments' is a list of dict containing details of each comment
        parsed_to_list_comments = [comment['snippet']['topLevelComment']['snippet'] for comment in comments]

        data = {
            "comments": parsed_to_list_comments,
            "next_page_token": next_page_token
        }

        return JsonResponse(data)
