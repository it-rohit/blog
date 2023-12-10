from .models import category
from assignment.models import Social_link

def get_Category(request):
    categories= category.objects.all()
    return dict (category=categories)

def get_Social_links (request):
    Social_links = Social_link.objects.all()
    # print(Social_links)
    return dict (Social_links = Social_links)