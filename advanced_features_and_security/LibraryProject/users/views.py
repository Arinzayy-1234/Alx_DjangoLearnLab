from django.shortcuts import render

# Create your views here.
def my_view(request):

    if request.user.has_perm('users.add_post'):
        pass

    else:
        pass