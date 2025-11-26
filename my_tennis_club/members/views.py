"""
Views for the 'members' app.

Purpose:
- Handle HTTP requests and return HTTP responses.
- Serve as the controller layer between models/templates and the user.
"""

from django.shortcuts import render          # Shortcut for rendering templates
from django.http import HttpResponse         # To return raw HTTP responses

# Basic view for members homepage
def members(request):
    """
    Purpose: Handle requests to the members homepage.

    Function:
    - Accepts an HTTP request object.
    - Returns a plain-text HTTP response.
    - Can later be extended to render templates with dynamic data.
    """
    return HttpResponse(
        "Hello from the members app! "
        "All members are welcome here. "
        "It is my tennis club. Enjoy your stay!"
    )
