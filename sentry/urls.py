from django.conf.urls import url, include
from allaccess.views import OAuthRedirect
from sentry.views import WPProviderCallbackView, WPProviderRedirect, LoginView, UnassignedUserView, AssignUsersFormView, AssignUserAutocomplete


urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'external/(?P<provider>\w+)/$', WPProviderRedirect.as_view(), name='externalLogin'),
    url(r'callback/(?P<provider>\w+)/$', WPProviderCallbackView.as_view(), name='callback'),
    url(r'users/$', AssignUsersFormView.as_view(), name='users'),
    url(r'users/autocomplete$', AssignUserAutocomplete.as_view(), name='users-autocomplete'),
    url(r'unassigned/$', UnassignedUserView.as_view(), name='unassigned')
]