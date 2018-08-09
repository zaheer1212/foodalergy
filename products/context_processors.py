from products.models import Category, Allergy

def categories_processor(request):
    try:
        categories = Category.objects.all().order_by('categoryName')
        return {'categories': categories}
    except:
        return {'categories': []}
        
def allergies_processor(request):
    try:
        allergies = Allergy.objects.all().order_by('allergyName')
        return {'allergies': allergies}
    except:
        return {'allergies': []}