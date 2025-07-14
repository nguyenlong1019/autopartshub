from django.utils.html import format_html 
from django.contrib.humanize.templatetags.humanize import intcomma 
import re 


def to_display_image_ext(url, desc):
    if url:
        return format_html('<a href="{}" target="_blank"><img src="{}" alt="{}" style="width: 40px;height: 40px;border-radius: 50%;border: 2px solid #fff;"/></a>', url, url, desc)
    return format_html('<img src="https://cdn-icons-png.flaticon.com/128/14534/14534501.png" alt="No image" style="width: 40px;height: 40px;border-radius: 50%;border: 2px solid #000;"/>', url, desc)


def to_display_image(url, desc):
    if url:
        return format_html('<img src="{}" alt="{}" style="width: 40px;height: 40px;border-radius: 50%;border: 2px solid #fff;"/>', url, desc)
    return format_html('<img src="/static/assets/images/noimage/no-picture-taking.png" alt="No image" style="width: 40px;height: 40px;border-radius: 50%;border: 2px solid #000;"/>', url, desc)


def to_blank_window(url, desc):
    return format_html('<a href="{}" target="_blank">{}</a>', url, desc)


def to_download_window(url, desc):
    return format_html('<a href="{}" download>{}</a>', url, desc)


def to_price_format(amount):
    try:
        return format_html("{} đ", intcomma(amount))
    except Exception:
        return "0 đ"
    

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

