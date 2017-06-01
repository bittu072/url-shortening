from django.conf import settings
from django.http import HttpResponseRedirect

# remove port 8000 in real implementation
DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.trialshort.com:8000")

def wildcard_redirect(request, path=None):
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)
