from django.conf.urls import include, url

from api.views import *
urlpatterns = [
    url(
        r"^profiles/$", ProfilesView.as_view() , name="user-profiles",
    ),
    url(
        r"^books/$", BooksView.as_view() , name="books",
    ),
    url(
        r"^loans/$", LoansView.as_view() , name="loans",
    ),
    url(
        r"^user/(?P<userid>-?\d+)/loans/$", UserLoansView.as_view() , name="user_loans",
    ),
    url(
        r"^user/(?P<userid>-?\d+)/profile/$", UserProfileView.as_view() , name="user_profile",
    ),

]