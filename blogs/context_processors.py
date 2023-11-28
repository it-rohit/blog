from .models import category


def get_Category(request):
    categories= category.objects.all()
    return dict (category=categories)