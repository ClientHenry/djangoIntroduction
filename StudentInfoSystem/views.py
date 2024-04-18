from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from StudentInfoSystem.forms import StudentForm
from StudentInfoSystem.models import Student
# Create your views here.
def any_name_1(request):
	current_students = Student.objects.all()
	return render(request, 'template_1.html', {'current_students_key': current_students})

def any_name_2(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			print('success')
			form.save()
			return HttpResponseRedirect(reverse('test1'))
	else:
		form = StudentForm()
	return render(request, 'template_2.html', {'form': form})
