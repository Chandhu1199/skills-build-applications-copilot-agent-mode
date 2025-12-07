"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import os

# Build a base URL using the CODESPACE_NAME environment variable when available
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    # Use the codespace preview URL format
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


def api_root_view(request):
    """Return a small JSON describing API endpoints using the computed base_url.

    This keeps the API root consistent across localhost and Codespaces preview URLs
    without modifying `views.py`.
    """
    return JsonResponse({
        'message': 'Welcome to OctoFit Tracker API',
        'version': '1.0.0',
        'endpoints': {
            'users': f"{base_url}/api/users/",
            'teams': f"{base_url}/api/teams/",
            'activities': f"{base_url}/api/activities/",
            'workouts': f"{base_url}/api/workouts/",
            'leaderboards': f"{base_url}/api/leaderboards/",
        }
    })


urlpatterns = [
    # Root returns the API root JSON built from the CODESPACE_NAME (if present)
    path('', api_root_view, name='api-root'),
    # Mount the API under /api/ so endpoints follow the required format
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

