"""
Project-level URL configuration for 'my_tennis_club'.

Purpose:
- Route incoming HTTP requests across the entire Django project.
- Delegate app-specific URL handling to the appropriate app.
- Define root path and admin path.
"""

# Import Django admin site functionality
from django.contrib import admin

# Import path() to define URL patterns and include() to include app URLs
from django.urls import path, include

# Import the 'members' view from the 'members' app to serve the homepage
from members.views import members

# Define the URL patterns for the project
urlpatterns = [
    path('', members),                       # Root URL '/' → members view (homepage)
    path('members/', include('members.urls')),  # '/members/' → delegated to members app URLs
    path('admin/', admin.site.urls),         # '/admin/' → Django admin interface
]
