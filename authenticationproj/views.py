from django.views.generic import DetailView
from django.contrib.auth import get_user_model

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"
