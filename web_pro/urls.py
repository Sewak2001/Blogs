"""web_pro URL Configuration

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
from django.urls import path
from web_app import views

admin.site.site_header = "Sewak's Blog Admin"
admin.site.site_title = "Sewak's Blog Admin Portal"
admin.site.site_title = "Welcome to Sewak's Blog"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/<str:name>',views.filtr,name='filter'),
    path('hom',views.home,name='home'),
    path('showblog',views.showb,name='showb'),
    path('formblog',views.formb,name='formb'),
    path('delete <int:id>',views.delete,name='delete'),
    path('update <int:id>',views.update,name='update'),
    path('signup',views.signup,name='sign'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('show',views.show,name='show'),
    path('read <int:id>',views.readmore,name='readmore'),
    path('showcontact',views.contact,name='showc'),
    path('formc',views.formc,name='formc'),
    path('showp',views.sprofile,name='showp'),
    path('edit',views.edit,name='edit'),
    path('showf',views.sfile,name='showf'),
    path('formf',views.ffile,name='formf'),
    path('updatei <int:id>',views.updatei,name='updatei'),
    path('deletei <int:id>',views.deletei,name='deletei'),
    path('',views.lbase,name='hbase'),   
    path('ads',views.adds,name='ads'),
    path('delete1 <int:id>',views.delete1,name='delete1'),
    path('update1 <int:id>',views.update1,name='update1'),
    path('search',views.search,name='search'),
    path('about',views.abouts,name='about'),
    path('change',views.change_password,name='change'),
    path("com",views.com,name="com"),
    path('comment/<int:id>',views.comment,name='comment'),
    path('deletecomment/<int:id>/<int:post_id>',views.deletecomment,name='deletecom'),
   
]
