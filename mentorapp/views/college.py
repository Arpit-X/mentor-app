from django.views import View
from onlineapp.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class CollegeView(View):

    def get(self, request, *args, **kwargs):
        college = College.objects.all()
        return render(
            request,
            template_name='college_data.html',
            context={
                'title': 'some shitty text',
                'dataSet': college,
                'user_permissions': self.request.user.get_all_permissions()
            }
        )



class CollegeListView(LoginRequiredMixin,ListView):
    login_url = '/login/'

    model = College
    context_object_name = 'dataSet'
    template_name = 'college_data.html'

    def get_context_data(self, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})

        return context


class CollegeWiseStudentListView(DetailView):
    model = College
    template_name = 'college_student_list.html'

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeWiseStudentListView, self).get_context_data(**kwargs)
        college = context.get('college')
        students = list(college.student_set.order_by('-mocktest1__total'))
        context.update({
            'heading': college.name,
            'dataSet': students,
            'user_permissions': self.request.user.get_all_permissions(),
            'collegeId':college.id
        })
        return context


class AddCollege(forms.ModelForm):

    class Meta:
        model = College
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter college Acronym'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter College Location'})
        }


class CreateAddCollegeView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = '/login/'
    permission_required = 'onlineapp.Add_college'
    permission_denied_message = "user doest have the permission to add the colleges"
    model = College
    form_class = AddCollege
    template_name = "add_college.html"
    success_url = reverse_lazy('mentorApp:college_html')
    def get_context_data(self, **kwargs):
        context = super(CreateAddCollegeView, self).get_context_data(**kwargs)
        context.update({

            'user_permissions': self.request.user.get_all_permissions()
        })
        return context



class AddMockTest(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'student', 'total']


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college']


class CreateStudentView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = '/login/'
    permission_required = 'onlineapp.add_student'
    permission_denied_message = "This user is not allowed to add the student"
    model = Student
    form_class = AddStudent
    template_name = 'add_student.html'
    success_url = reverse_lazy('college_data.html')

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        second_form = AddMockTest()
        context.update({
            'secondForm': second_form,
            'user_permissions':self.request.user.get_all_permissions()
        })
        return context

    def post(self, request, *args, **kwargs):
        import ipdb
        student_form = AddStudent(request.POST)
        mock_form = AddMockTest(request.POST)
        # ipdb.set_trace()
        if student_form.is_valid():
            college = get_object_or_404(College, **kwargs)
            # ipdb.set_trace()
            student = student_form.save(commit=False)
            # ipdb.set_trace()
            student.college = college
            student.save()

        if mock_form.is_valid():
            mockTest = mock_form.save(commit=False)
            # ipdb.set_trace()
            mockTest.student = student
            # ipdb.set_trace()
            mockTest.total = sum(mock_form.cleaned_data.values())
            mockTest.save()

        return redirect('mentorApp:college_wise_student_list', id=college.id);


class UpdateCollege(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    permission_required = 'onlineapp.change_college'
    permission_denied_message = "This user is not allowed to change the college"
    model = College
    form_class = AddCollege
    template_name = "add_college.html"
    success_url = reverse_lazy('mentorApp:college_html')

    def get_context_data(self, **kwargs):
        context = super(CollegeWiseStudentListView, self).get_context_data(**kwargs)
        context.update({

            'user_permissions': self.request.user.get_all_permissions()
        })
        return context


class DeleteCollege(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = '/login/'
    permission_required = 'onlineapp.delete_college'
    permission_denied_message = "This user is not allowed to delete the college"
    model = College
    template_name = 'confirm.html'
    success_url = reverse_lazy('mentorApp:college_html')

    def get_context_data(self, **kwargs):
        context = super(CollegeWiseStudentListView, self).get_context_data(**kwargs)
        context.update({

            'user_permissions': self.request.user.get_all_permissions()
        })
        return context


class UpdateStudent(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    permission_required = 'onlineapp.change_student'
    permission_denied_message = "This user is not allowed to change the student"
    model = Student
    form_class = AddStudent

    def get_context_data(self, **kwargs):
        context = super(UpdateStudent, self).get_context_data(**kwargs)
        student = get_object_or_404(Student, **self.kwargs)
        second_form = AddMockTest(instance=student.mocktest1)
        context.update({
            'secondForm': second_form,
            'user_permissions':self.request.user.get_all_permissions()
        })
        return context

    def post(self, request, *args, **kwargs):
        import ipdb
        student = get_object_or_404(Student, **self.kwargs)
        student_form = AddStudent(request.POST, instance=student)
        mock_form = AddMockTest(request.POST, instance=student.mocktest1)
        #ipdb.set_trace()
        if student_form.is_valid():
            tmp = get_object_or_404(Student, **kwargs)
            #ipdb.set_trace()
            student = student_form.save(commit=False)
            #ipdb.set_trace()
            student.college = tmp.college
            student.save()

        if mock_form.is_valid():
            mockTest = mock_form.save(commit=False)
            #ipdb.set_trace()
            mockTest.student = student
            mockTest.total = sum(mock_form.cleaned_data.values())
            mockTest.save()
        return redirect('mentorApp:college_wise_student_list', student.college.id);

    # template_name = "add_student.html"
    # success_url = reverse_lazy('mentorApp:college_wise_student_list',**kwargs)


class DeleteStudent(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = '/login/'
    permission_required = 'onlineapp.delete_college'
    permission_denied_message = "This user is not allowed to delete the student"
    model = Student
    template_name = "confirm.html"
    def get_context_data(self, **kwargs):
        context = super(CollegeWiseStudentListView, self).get_context_data(**kwargs)
        context.update({

            'user_permissions': self.request.user.get_all_permissions()
        })
        return context

    def get_success_url(self):
        student = get_object_or_404(Student, **self.kwargs)

        return reverse_lazy('mentorApp:college_wise_student_list', kwargs={'id': student.college.id})
