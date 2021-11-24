# Headers
from rest_framework import routers
from Locations.views import LocationsViewSet

# Define Route
router = routers.DefaultRouter()
router.register('assignment',LocationsViewSet)
