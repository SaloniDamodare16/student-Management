from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Student
from django.db.models import Avg  
from .forms import StudentForm


# ================= HOME =================

def home(request):
    total_students = Student.objects.count()

    average_age = Student.objects.aggregate(
        Avg('age')
    )['age__avg']

    recent_students = Student.objects.order_by('-id')[:5]

    return render(request, 'students/home.html', {
        'total_students': total_students,
        'average_age': average_age,
        'recent_students': recent_students,
    })


# ================= STUDENT LIST =================

def student_list(request):

    students = Student.objects.all()

    search = request.GET.get('search')

    if search:
        students = students.filter(name__icontains=search)

    return render(request, 'students/student_list.html', {
        'students': students,
        'search': search
    })


# ================= ADD STUDENT =================

def student_add(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Student added successfully!'
            )

            return redirect('student_list')

    else:

        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student'
    })


# ================= EDIT STUDENT =================

def student_edit(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Student updated successfully!'
            )

            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student'
    })


# ================= DELETE STUDENT =================

def student_delete(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()

        messages.success(
            request,
            'Student deleted successfully!'
        )

        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })


# ================= ABOUT =================

def about(request):

    return render(request, 'students/about.html')


# ================= CONTACT =================

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        messages.success(
            request,
            f'Thank you {name}! Your message has been received.'
        )

        return redirect('contact')

    return render(request, 'students/contact.html')