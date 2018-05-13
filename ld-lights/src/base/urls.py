from django.conf import settings
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from base import views

urlpatterns = [
    # catch all others because of how history is handled by react router
    # cache this page because it will never change
    url(
        r'',
        cache_page(
            settings.PAGE_CACHE_SECONDS
        )(views.IndexView.as_view()),
        name='index'
    ),
]
