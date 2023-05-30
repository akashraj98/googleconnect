from django.urls import path
from rest import views

urlpatterns=[
  path('v1/calendar/init/', views.GoogleCalenderInit.as_view(), name='google_permission'),
  path('v1/calendar/redirect/', views.GoogleCalendarRedirect.as_view(), name='google_redirect')
]