from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Users

def index(request):

	if request.method == 'GET':

		if request.GET.get('uid', False) == False:
			
			data = Users.objects.all()

			return render(request, 'index.html', {'data':data})

		else:

			user = Users.objects.filter(pk=request.GET["uid"])

			if not user:
				messages.error(request, 'No such records found!')
				return redirect('home')
			else:
				user = user.get()

			data = Users.objects.all()

			return render(request, 'index.html', {'data':data, 'user':user})


	elif request.method == 'POST':

		user_name = request.POST['record']

		usr = Users(name=user_name)

		usr.save()

		return redirect('home')

def delete(request):
	
	if request.method == 'GET':
		
		user_id = request.GET['id']

		user = Users.objects.filter(pk=user_id)

		if not user:
			messages.error(request, 'No such records found!')
			return redirect('home')
		else:
			user = user.delete()

		return redirect('home')

def update(request):
	
	if request.method == 'POST':
		
		user_id = request.GET['uid']

		user_name = request.POST['record']

		usr = Users.objects.filter(pk=user_id)

		if not usr:
			messages.error(request, 'No such records found!')
			return redirect('home')
		else:
			usr = usr.get()

		usr.name = user_name

		usr.save()

		return redirect('home')









