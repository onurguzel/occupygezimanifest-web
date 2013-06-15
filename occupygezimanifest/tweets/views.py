from django.http import HttpResponse
from django.template import Context, loader

from tweets.models import Tweet


def index(request):
    manifest_items = Tweet.objects.all().order_by('-id')
    template = loader.get_template('index.html')
    context = Context({
        'manifest_items': manifest_items,
    })
    return HttpResponse(template.render(context))
