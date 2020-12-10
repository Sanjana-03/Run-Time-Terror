from django.forms import ModelForm
from django import forms
from .models import *

class AdminForm(forms.ModelForm):
  class Meta:
    model = Admin
    fields ='__all__'

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields='__all__'

class QuizForm(forms.ModelForm):
	class Meta:
		model=Quiz
		fields=( 'id','name','admin_id','status')

class QuestionForm(forms.ModelForm):
	class Meta:
		model=Question
		fields=('__all__')

class AttemptForm(forms.ModelForm):
	class Meta:
		model=Attempt
		fields=('__all__')

class AnswerForm(forms.ModelForm):
	class Meta:
		model=Question
		fields=('id','answer')




