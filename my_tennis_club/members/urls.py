"""
App-level URL configuration for 'members' app.

Purpose:
- Define URLs specific to the 'members' app.
- Keep app routing self-contained and reusable.
"""

from django.urls import path   # Import path to define URL routes
from . import views            # Import views from the current app

# Define URL patterns for the app
urlpatterns = [
    path('', views.members, name='members-home'),  # /members/ → members view
    # Future app routes can be added here:
    # path('create/', views.create_member, name='create-member')
    # path('<int:id>/', views.member_detail, name='member-detail')
]
