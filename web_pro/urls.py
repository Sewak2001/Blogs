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
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

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
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('reset-password', PasswordResetView.as_view(), name='password_reset'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    # path('reset-password/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('password_change_done/', views.password_change_done, name='password_change_done'),
   
]
