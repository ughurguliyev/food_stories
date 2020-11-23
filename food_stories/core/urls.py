from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('about/', views.AboutPage.as_view(), name='about-page'),
    path('stories/', views.StoriesPage.as_view(), name='stories-page'),
    path('recipes/', views.RecipesPage.as_view(), name='recipes-page'),
    path('contact/', views.ContactPage.as_view(), name='contact-page'),
    path('article/<slug>/', views.ArticleDetailPage.as_view(), name='article-detail-page'),
    path('login/', views.CustomLogInPage.as_view(), name='login-page'),
    path('logout/', views.LogOutPage.as_view(), name='logout-page'),
    path('register/', views.RegisterPage.as_view(), name='register-page'),
    path('account/', views.AccountPage.as_view(), name='account-page'),
    path('create_story/', views.CreateArticlePage.as_view(), name='create-story-page')
]