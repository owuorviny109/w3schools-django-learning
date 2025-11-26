"""
Views for the 'members' app.

Purpose:
- Handle HTTP requests and return HTTP responses.
- Serve as the controller layer between models/templates and the user.
- Demonstrates rendering HTML templates instead of returning raw text.
"""

# Import HttpResponse to send an HTTP response to the browser
from django.http import HttpResponse

# Import loader to load templates manually
from django.template import loader

# View function for members homepage
def members(request):
    """
    Purpose: Handle requests to the members homepage and render an HTML template.

    Function:
    - Accepts an HTTP request object.
    - Loads the 'myfirst.html' template from the templates directory.
    - Renders the template and returns it as an HttpResponse.
    - Can later include dynamic context data for template rendering.
    """
    
    # Load the template file 'myfirst.html' from the templates directory
    template = loader.get_template('myfirst.html')
    
    # Render the template (currently no context dictionary passed) and return as HTTP response
    return HttpResponse(template.render())
