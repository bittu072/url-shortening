from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # this is to redirect just "blog.abcd.com" url
    host(r'blog', 'urlshort.hostsconf.urls', name='blog'),

    # this is to redirect any prefix url "xx.abcd.com"
    host(r'(?!www).*', 'urlshort.hostsconf.urls', name='wildcard'),
)
