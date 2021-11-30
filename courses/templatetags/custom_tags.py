from django import template
from ..models import Course

register = template.Library()


@register.simple_tag
def courses(category):
    return Course.objects.filter(category=category)


@register.simple_tag
def course_details(category):
    course = Course.objects.filter(category__name=category)
    course_name = []
    for i in course:
        course_name.append(i.name)
    return course_name


@register.simple_tag
def enrolled(course_id):
    return Course.objects.get(id=course_id).name


@register.simple_tag
def bookmarked_course(course_id):
    return Course.objects.get(id=course_id).name


@register.simple_tag
def convert(value):
    return str(value)


@register.simple_tag
def zero_or_one(categories, value):
    if 0 <= categories.index(value) <= 1:
        return True


@register.simple_tag
def two_or_three(categories, value):
    if 2 <= categories.index(value) <= 3:
        return True


@register.simple_tag
def get_item(dictionary):
    return dictionary['snippet']['topLevelComment']['snippet']


@register.simple_tag
def get_dict_details(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def get_list_details(list_, item):
    return list_[item]


@register.filter
def extract_date(value):
    date, time = value.split('T')
    return date


@register.filter
def separate_star(value):
    separated = value.split('*')
    return separated

