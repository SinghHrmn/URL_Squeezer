from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SqueezeURL
# Create your views here.


def render_shortcode(request, shortcode=None):
    obj = get_object_or_404(SqueezeURL, short_code=shortcode)
    return HttpResponse(f"Mapped URl is {obj.url}")