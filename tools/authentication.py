"""
Например, если вы обрабатываете электронные письма с двойным подтверждением и
Вы не хотите разрешать пользователям без верифицированного
адреса электронной почты входить в ваше приложение, вы можете сделать что-то вроде этого:
"""


# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
	def confirm_login_allowed (self, user):
		if not user.is_activate or not user.is_activated:
			raise forms.ValidationError("Возникла проблема с вашим login'ном ", code='invalid_login')


# urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

urlpatterns	= [
	url(r'^login/$', auth_views.login, {'template_name': 'core/login.html',
		'authentication_form': CustomAuthenticationForm}, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
]