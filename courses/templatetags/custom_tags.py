from django import template
from ..models import Course
from ..views import channel_details_url, video_details_url

register = template.Library()

@register.simple_tag
def get_item(dictionary):
    return dictionary['snippet']['topLevelComment']['snippet']


@register.simple_tag
def get_dict_details(dictionary, key):
    return dictionary.get(key) if type(dictionary) == dict else None


@register.simple_tag
def get_list_details(list_, item):
    return list_[item] if len(list_) > item else None


@register.simple_tag
def get_video_details(video_id):
    return video_details_url(video_id)


@register.filter
def extract_date(value):
    date, time = value.split('T')
    return date


@register.filter
def separate_star(value):
    separated = value.split('*')
    return separated


@register.simple_tag
def courses():
    youtube_courses = Course.objects.all()
    return youtube_courses

