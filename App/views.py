from django.shortcuts import render,redirect
from .models import *
from .forms import *
import time
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def index(request):
	return render(request,'index.html');

def login(request):
	return render(request,'login.html');

def signup(request):
	return render(reuqest,'signup.html');

def home(request):
	quizes =Quiz.objects.all()
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime()) 
	print(current)
	for quiz in quizes:
		if str(quiz.status)==str(current):
			quiz.status="Live"
			print(quiz.status)
		elif str(quiz.status)>str(current):
			quiz.status="Upcoming"
			print(quiz.status)
		else:
			quiz.status="Past"
			print(quiz.status)
	form = QuizForm(quizes, many=True)
	return render(reuqest,'home.html')


'''@api_view(['GET'])
def Check(request,id,pk):
	user_id= User.objects.get(id=id)
	ques_id=Question.objects.get(id=pk)
	exist=Attempt.objects.filter(user=user_id,qid=ques_id)
	msg={'user':str(user_id),'quesid':str(ques_id)}
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime()) 
	if not exist:
		return Response(msg,status=HTTP_200_OK)
	else:
		return Response(status=HTTP_400_BAD_REQUEST)


def UserAttempt(request,id,pk):
	user_id= User.objects.get(id=id)
	ques_id=Question.objects.get(id=pk)
	status=ques_id.quiz_id.status
	print('status='+str(status))
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime())
	if str(status)==str(current):

		form =AttemptForm()
		if form.is_valid():
			
			form.save()
			return render(serializer.data,status=HTTP_200_OK)
		else:
			return Response(status=HTTP_400_BAD_REQUEST)

'''


def ViewQuestions(request,pk):
	questions =Question.objects.get(quiz_id=pk)
	return render(request,'questions.html')













