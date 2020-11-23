from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login as auth_login

from .forms import ContactForm, RegisterForm, LogInForm, ArticleCreationForm
from .models import Contact, Article, Category

User = get_user_model()

class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context = {
            'user': self.request.user
        }
        return context


class StoriesPage(TemplateView):
    template_name = 'strories.html'


class RecipesPage(TemplateView):
    template_name = 'recipes.html'


class ContactPage(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        Contact.objects.create(
            name = form.cleaned_data.get('name'),
            email = form.cleaned_data.get('email'),
            subject = form.cleaned_data.get('subject'),
            message = form.cleaned_data.get('message')
        )
        return HttpResponseRedirect(self.get_success_url())


class ArticleDetailPage(DetailView):
    model = Article
    template_name = 'single.html'
    context_object_name = 'article'


class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        new_user = User(
            name = form.cleaned_data.get('name'),
            surname = form.cleaned_data.get('surname'),
            email = form.cleaned_data.get('email'),
            is_active = True,
            is_superuser = True,
            is_staff = True
        )
        new_user.set_password(form.cleaned_data.get('password'))
        new_user.save()
        
        return HttpResponseRedirect(self.get_success_url())

class CreateArticlePage(LoginRequiredMixin, FormView):
    form_class = ArticleCreationForm
    template_name = 'create_story.html'
    success_url = '/'
    login_url = 'login-page'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        category = form.data.get('options')
        
        new_article = Article(
            title = title,
            body = description
        )
        new_article.save()

        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super(CreateArticlePage, self).get_context_data(**kwargs)
        context['choices'] = Category.objects.all()
        return context
        

class CustomLogInPage(FormView):
    template_name = 'accounts/login.html'
    form_class = LogInForm

    def get_success_url(self):
        return reverse('home-page')
    
    def check_email(self, form):
        email = form.cleaned_data.get('email')
        valid_email = User.objects.filter(email=email).first()
        return valid_email
    
    def check_password(self, user, form):
        password = form.cleaned_data.get('password')
        return user.check_password(password)
    
    def form_valid(self, form):
        user = self.check_email(form=form)
        if user:
            is_valid_password = self.check_password(user=user, form=form)
            if is_valid_password:
                auth_login(self.request, user)
                return super().form_valid(form)
        return super().form_valid(form)


class LogOutPage(LogoutView):
    def get_next_page(self):
        return reverse('home-page')


class AccountPage(LoginRequiredMixin, TemplateView):
    template_name = 'user-profile.html'
    login_url = 'login-page'

    def get_context_data(self, *args, **kwargs):
        context = super(AccountPage, self).get_context_data(*args, **kwargs)
        context = {
            'user': self.request.user
        }
        return context

   