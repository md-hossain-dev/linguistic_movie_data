from django.urls import path
from .views import ProcessTextView

urlpatterns = [
    path('process-text/', ProcessTextView.as_view(), name='process-text'),
]
