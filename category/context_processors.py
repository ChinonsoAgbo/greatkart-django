


from .models import Category


def menu_links(request):
  links = Category.objects.all() # store all category in the links 
  return dict(links = links) # return all links in the category 
