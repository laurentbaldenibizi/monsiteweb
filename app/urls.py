"""monsiteweb URL Configuration

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
from django.urls import include, path
from app.views import home,categories,users,publication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index, name='home'),

    path('categories/', categories.index, name='categories_index'),
    path('categories/create', categories.create, name='categories_create'),
    path('categories/store', categories.store, name='categories_store'),
    path('categories/edit/<int:id>', categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),

path('login/', users.user_login, name='users_login'),
      path('logout/', users.user_logout, name='logout'),
       path('users/', users.index, name='users_index'),
    path('register/', users.register, name='users_register'),
    path('users/store', users.store, name='users_store'),
    path('users/delete/<int:id>', users.delete, name='users_delete'),


    path('publication/', publication.index, name='publication_index'),
    path('publication/create', publication.create, name='publication_create'),
    path('publication/store', publication.store, name='publication_store'),
    path('publication/edit/<int:id>', publication.edit, name='publication_edit'),
    path('publication/delete/<int:id>', publication.delete, name='publication_delete'),

]
