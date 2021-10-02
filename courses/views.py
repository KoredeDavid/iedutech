import os

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View

from .forms import NewsLetterForm
from .models import Category, Course


def test(request):
    return render(request, 'test.html',)


class Index(View):
    def get(self, request):
        global res
        form = NewsLetterForm()
        categories = list(Category.objects.all())
        favourites = request.session.get('favourites', [])
        print(favourites)
        context = {
            'categories': categories,
            'favourites': favourites,
            'form': form
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = NewsLetterForm(request.POST)
        categories = list(Category.objects.all())
        favourites = request.session.get('favourites', [])
        context = {
            'categories': categories,
            'favourites': favourites,
            'form': form
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            form.save()
            subject = 'KoredeDavid from EduTech'
            message = f'Hi {name.capitalize()}, I just want to say thank you for signing up for our News Letter. We ' \
                      f'are committed to serving you with  our latest gist '
            if os.environ.get('DJANGO_ENV', '') == 'production':
                email_from = os.environ.get('EMAIL_HOST_USER', '')
            else:
                email_from = 'test@email.com'
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list, )
            messages.success(request, f'Thank you {name.capitalize()}')
            return redirect('/#news')
        return render(request, 'index.html', context)


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
        return render(request, 'test.html')
