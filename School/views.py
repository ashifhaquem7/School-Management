from django.shortcuts import render,redirect
from .forms import AdminSignupForm,TeachersignupForm,StudentSignupForm,edit_TeacherForm,edit_StudentForm,NoticeForm,AttendenceForm,AskDateForm,ContactusForm
from .models import CustomUser,Teacher,Student,Attendence,Notice
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request,'school/index.html')

def aboutUs(request):
    return render(request,'school/aboutus.html')

def contactUs(request):
    form=ContactusForm()
    context={
        'form':form,
    }
    return render(request,'school/contactus.html',context)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def login_view(request):
    return render(request,'school/adminlogin.html')


################################# Admin Panel ###############################

def adminSignup(request):
    form = AdminSignupForm()
    context = {
        'form' : form,
    }
    return render(request,'school/adminsignup.html', context)

def admin_signup(request):
    if request.method=='POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,is_superuser=1,is_staff=1,role_id=1)
            user.save()
            print('Admin added successfully!!')
         
            return redirect('adminlogin')
    return render(request,'school/adminsignup.html')




################################### Teacher ##############################

def teacherSignup(request):
    form = TeachersignupForm()
    context = {
        'form' : form,
    }
    return render(request,'school/teachersignup.html',context)

def teacherwaitApproval(request):
    teachers=Teacher.objects.get(id=request.user.id)
    return render(request,'school/teacher_wait_for_approval.html',{'teachers':teachers})

def teachersave(request):
    if request.method == 'POST':
        form = TeachersignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            mobile= form.cleaned_data['mobile']
            salary = form.cleaned_data['salary']
            
            try:
                new = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,is_active=0,is_staff=1,role_id=66)
                new.teacher.mobile = mobile
                new.teacher.salary = salary
                new.teacher.status = 'F'
                new.save()
                print('successful')
                return redirect('teacher-wait-for-approval')
            # except Exception as e:
            #     print(f'Error:{e}')
            #     return redirect('teachersignup')
            except IntegrityError as e:
                print(f'Error:{e}')
                return HttpResponse('<h2>Integrity Error</h2>')
        else:
            print(form.errors)
            return HttpResponse('<h2>Invalid</h2>')
    else:
            return HttpResponse('<h2>Out</h2>')
    



################################# Student ##############################

def studentSignup(request):
    form= StudentSignupForm()
    context = {
        'form': form,
    }
    return render(request,'school/studentsignup.html', context)

def studentWaitApproval(request):
    students=Student.objects.get(id=request.user.id)
    return render(request,'school/student_wait_for_approval.html',{'students':students})

def student_signup(request):
    if request.method=='POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            mobile = form.cleaned_data['mobile']
            class1 = form.cleaned_data['class1']
            roll = form.cleaned_data['roll']
            fee = form.cleaned_data['fee']

            try:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name,username=username,password=password,role_id=99,is_active=0)
                user.student.mobile = mobile
                user.student.class1 = class1
                user.student.roll = roll
                user.student.fee = fee
                user.student.status = 'F'
                user.save()
                print('successful')
                messages.success(request,'Student Added Successfully!')
                return redirect('student-wait-approval')
            except IntegrityError as e:
                print(f'Error:{e}')
                return HttpResponse('<h2>Integrity Error</h2>')
            except Exception as e:
                print(f'Error:{e}')
                return HttpResponse('<h2>Exception Error</h2>')
        else:
            print(form.errors)
            messages.error(request,'Invalid Credentials!!')
            return HttpResponse('<h2>Invalid</h2>')

################################## Login Authentication #####################
        
@login_required(login_url='login')
#@user_passes_test(is_admin)
def admin_dashboard(request):
    teachercount= Teacher.objects.all().filter(status='T').count()
    studentcount = Student.objects.all().filter(status='T').count()
    salary = Teacher.objects.all().filter(status='T').aggregate(Sum('salary'))
    tp=salary['salary__sum']
    new_salary = float(tp)
    studentfee = Student.objects.all().filter(status='T').aggregate(Sum('fee'))
    new_fee = float(studentfee['fee__sum'])
    pendingteacher = Teacher.objects.all().filter(status='F').count()
    pendingstudent = Student.objects.all().filter(status='F').count()
    teachersalary = Teacher.objects.filter(status='F').aggregate(Sum('salary'))
    pendingteachersalary= float(teachersalary['salary__sum'] or 0)
    studentfee = Student.objects.all().filter(status='F').aggregate(Sum('fee'))
    pendingstudentfee = float(studentfee['fee__sum'] or 0)
    notices= Notice.objects.all()
    context={
        'teachercount' : teachercount,
        'studentcount' : studentcount,
        'new_salary' : new_salary,
        'new_fee' : new_fee,
        'pendingteacher' : pendingteacher,
        'pendingstudent' : pendingstudent,
        'pendingteachersalary' : pendingteachersalary,
        'pendingstudentfee' : pendingstudentfee,
        'notices': notices,
    }
    return render(request,'school/admin_dashboard.html', context)

def teacher_dashboard(request):
    teachers=Teacher.objects.get(id=request.user.id)
    notices= Notice.objects.all()
    context={
        'teachers': teachers,
        'notices': notices,
    }
    return render(request,'school/teacher_dashboard.html', context)

def student_dashboard(request):
    students = Student.objects.get(id=request.user.id)
    notices= Notice.objects.all()
    context={
        'students':students,
        'notices': notices,
    }
    return render(request,'school/student_dashboard.html',context)

def dologin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        try:
            if user.is_superuser and user.is_staff and user.is_active:
                login(request,user)
                return redirect('admin-dashboard')
            elif user.is_staff and user.role_id=='66' and not user.is_superuser:
                login(request,user)
                return redirect('teacher-dashboard')
            elif user.is_active and user.role_id=='99' and not user.is_superuser and not user.is_staff:
                login(request,user)
                return redirect('student-dashboard')
            else:
                return HttpResponse('<h2>Invalid</h2>')
        except ObjectDoesNotExist as e:
            # Handle the case where the user object does not exist
            print(f'Error: {e}')
            return HttpResponse('<h2>User not found</h2>')
        except IntegrityError as e:
            print(f'Error:{e}')
            return HttpResponse('<h2>Integrity Error</h2>')
        except:
            messages.error(request,'Invalid Credentials!!')
            return HttpResponse('<h2>Invalid Login Credentials!</h2>')
    
def logout_request(request):
    messages.success(request,'Logout')
    return redirect('login')
################################## end of Login #######################

@login_required
def adminstudent(request):
    return render(request,'school/admin_student.html')

@login_required
def adminfee(request):
    students=Student.objects.all()
    context={
        'students' : students,
    }
    return render(request,'school/admin_fee.html',context)

@login_required
def adminViewFee(request,class1):
    students=Student.objects.all()
    studentsfee = Student.objects.filter(class1=class1)
    context={
        'students' : students,
        'studentsfee':studentsfee,
        'class1': class1
    }
    return render(request,'school/admin_view_fee.html',context)


################################ Admin-teacher ######################

####################### (View All Teacher) #########################
@login_required
def adminteacher(request):
    return render(request,'school/admin_teacher.html') 

@login_required
def adminVteacher(request):
    teachers=Teacher.objects.all()
    context={
        'teachers' : teachers,
    }
    return render(request,'school/admin_view_teacher.html',context)

@login_required        
def adminTeacher_edit(request,id):
    request.session['id']= id

    teachers=Teacher.objects.get(id=id)
    form=edit_TeacherForm()
    # filling the form with Data from database #
    form.fields['first_name'].initial = teachers.user.first_name
    form.fields['last_name'].initial = teachers.user.last_name
    form.fields['mobile'].initial = teachers.mobile
    form.fields['salary'].initial = teachers.salary
    context={
        'form':form,
        'id':id,
    }
    return render(request,'school/admin_update_teacher.html',context)

@login_required
def adminTeacher_save(request):
    id = request.session.get('id')
    print(id)
    form=edit_TeacherForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        mobile = form.cleaned_data['mobile']
        salary = form.cleaned_data['salary']

        try:
            user = CustomUser.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            try:
                teacher_model = Teacher.objects.get(id=id)
                teacher_model.mobile=mobile
                teacher_model.salary=salary
                teacher_model.save()
                print('Updated Successfully!!!')
                messages.success(request,'Teacher Updated Successfully')
                return redirect('admin-view-teacher')
            except Teacher.DoesNotExist:
                print('Teacher does not exist!')
                messages.error(request,'Teacher Does not exist!!')
                return HttpResponse('<h2>Not exist</h2>')
        except IntegrityError as e:
            print(f'Error:{e}')
            #return redirect('/edit-admin-teacher/'+id)
            return HttpResponse('<h2>Integrity Error</h2>')
    else:
        print(form.errors)
        return redirect('edit-admin-teacher/'+id)

@login_required      
def adminTeacher_enable(request,id):
    teacher=Teacher.objects.get(id=id)
    try:
        teacher.status ='T'
        teacher.user.is_active = 1
        teacher.save()
        print('enabled Succcessfull!!')
        messages.success(request,'Teacher Enabled ')
        return redirect('admin-view-teacher')
    except:
        print('Not enabled')
        messages.error(request,'Failed to Enable')
        return redirect('admin-view-teacher')

@login_required   
def disable_adminTeacher(request,id):
    teachers=Teacher.objects.get(id=id)
    try:
        teachers.status='F'
        teachers.user.is_active=0
        teachers.save()
        messages.success(request,'Teacher Disabled')
        print('Disabled!!')
        messages.error(request,'Failed to Disable')
        return redirect('admin-view-teacher')
    except:
        print('Not')
        return redirect('admin-view-teacher')

@login_required   
def deleteAdminTeacher(request,id):
    Atecaher= Teacher.objects.get(id=id)
    try:
        Atecaher.delete()
        print('Deleted Successful!!')
        messages.success(request,'Teacher Deleted!!')
        return redirect('admin-view-teacher')
    except:
        print('Failed to Delete')
        messages.error(request,'Failed to Delete')
        return redirect('admin-view-teacher')

############## end of (view all teacher) ###################


def adminNotice_view(request):
    form = NoticeForm()
    if request.method=='POST':
        form= NoticeForm(request.POST)
        if form.is_valid():
            notice_instance = form.save(commit=False)
            notice_instance.by = request.user.first_name
            print('by-',notice_instance.by)
            notice_instance.save()
            return redirect('admin-dashboard')
        else:
            print(form.errors)
            print('error')
    return render(request,'school/admin_notice.html',{'form':form})

#################### (Admin-add-Teacher-Panel) #################
@login_required
def adminAddteacher(request):
    form = TeachersignupForm()
    context={
        'form':form,
    }
    return render(request,'school/admin_add_teacher.html',context)

@login_required
def adminAddTeacher_view(request):
    if request.method=='POST':
        form = TeachersignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile = form.cleaned_data['mobile']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            salary = form.cleaned_data['salary']
            try:
                user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,is_active=1,is_staff=1,role_id=66)
                user.teacher.mobile=mobile
                user.teacher.salary=salary
                user.teacher.status='T'
                user.save()
                messages.success(request,'Teacher Added')
                redirect('admin-view-teacher')
            except IntegrityError as e:
                print(f'Error:{e}')
                return HttpResponse('<h2>Integrity Error</h2>')
        else:
            print(form.errors)
            messages.error(request,'Failed to Add')
            redirect('admin-add-teacher')
##################### End of (admin add Teacher Panel) ###############
            

################ (Admin Approve Teacher) ############
@login_required            
def adminApproveteacher(request):
    teachers=Teacher.objects.filter(status='F')
    context={
        "teachers":teachers,
    }
    return render(request,'school/admin_approve_teacher.html',context)

@login_required      
def teacher_approve(request,id):
    teacher=Teacher.objects.get(id=id)
    try:
        teacher.status ='T'
        teacher.user.is_active = 1
        teacher.save()
        print('enabled Succcessfull!!')
        messages.success(request,'Teacher Enabled ')
        return redirect('admin-approve-teacher')
    except:
        print('Not enabled')
        messages.error(request,'Failed to Enable')
        return redirect('admin-approve-teacher')

@login_required   
def teacher_remove(request,id):
    teachers=Teacher.objects.get(id=id)
    try:
        teachers.status='F'
        teachers.user.is_active=0
        teachers.save()
        messages.success(request,'Teacher Disabled')
        print('Disabled!!')
        messages.error(request,'Failed to Disable')
        return redirect('admin-approve-teacher')
    except:
        print('Not')
        return redirect('admin-approve-teacher')

################### end of (Admin Approve Teacher) ####################


################ (admin Teacher Attendance) ################# 
@login_required
def adminTeacherAttendance(request):
    pass

##################### end of (admin Teacher Attendance) ##################

####################### (Admin View Salary pandel) #############
@login_required
def adminViewTechSalary(request):
    teachers=Teacher.objects.all()
    context={
        'teachers':teachers,
    }
    return render(request,'school/admin_view_teacher_salary.html',context)

######################## end of (Admin View Salary pandel) ##################



########################## Admin-student ########################
@login_required
def adminVstudent(request):
    students=Student.objects.all()
    context={
        'students':students,
    }
    return render(request,'school/admin_view_student.html',context)

@login_required
def adminAddstudent(request):
    form=StudentSignupForm()
    context={
        'form': form,
    }
    return render(request,'school/admin_add_student.html',context)

@login_required
def adminAddStudent_view(request):
    if request.method=='POST':
        form=StudentSignupForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            mobile=form.cleaned_data['mobile']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            roll = form.cleaned_data['roll']
            class1=form.cleaned_data['class1']
            fee=form.cleaned_data['fee']
            try:
                user=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,is_active=1,role_id=99)
                user.student.mobile=mobile
                user.student.roll=roll
                user.student.class1=class1
                user.student.fee=fee
                user.student.status ='T'
                user.save()
                print('successful!!')
                messages.success(request,'Student Added!')
                return redirect('admin-view-student')
            except IntegrityError as e:
                print(f'Error:{e}')
                return HttpResponse('<h2>Integrity Error</h2>')
        else:
            print('Not working')
            messages.error(request,'Failed to Add!')
            redirect('admin-add-student')
    else:
        return HttpResponse('<h2>Invalid</h2>')

@login_required
def edit_adminStudent(request,id):
    request.session['id']=id
    student = Student.objects.get(id=id)
    form = edit_StudentForm()
    form.fields['first_name'].initial = student.user.first_name
    form.fields['last_name'].initial = student.user.last_name
    form.fields['mobile'].initial = student.mobile
    form.fields['roll'].initial = student.roll
    form.fields['class1'].initial = student.class1
    form.fields['fee'].initial = student.fee

    context ={
        'form' : form,
        'id' : id
    }
    return render(request,'school/admin_update_student.html', context)

@login_required
def edit_adminStudent_save(request):
    id =request.session.get('id')
    form = edit_StudentForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        mobile= form.cleaned_data['mobile']
        roll = form.cleaned_data['roll']
        class1 = form.cleaned_data['class1']
        fee = form.cleaned_data['fee']
        try:
            user = CustomUser.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            try:
                students = Student.objects.get(id=id)
                students.mobile=mobile
                students.roll=roll
                students.class1=class1
                students.fee = fee
                students.save()

                print('Updated Successfully!!')
                messages.success(request,'Student Updated!')
                return redirect('admin-view-student')
            except Student.DoesNotExist:
                print('Not Exist')
                return HttpResponse('<h2>Student Does not exist!!</h2>')
            
        except IntegrityError as e:
            print(f'Error:{e}')
            return HttpResponse('<h2>Integrity Error</h2>')
    else:
        print(form.errors)
        messages.error(request,'Failed to Add')
        return redirect('edit-admin-student/'+id)

@login_required
def enable_adminStudent(request,id):
    students = Student.objects.get(id=id)
    try:
        students.status='T'
        students.user.is_active=1
        students.save()
        print('Enabled!!')
        messages.success(request,'Student Enabled')
        return redirect('admin-view-student')
    except:
        print('Not Enable')
        messages.error(request,'Failed to Enable!')
        return redirect('admon-view-student')
    
@login_required    
def disable_adminStudent(request,id):
    students= Student.objects.get(id=id)
    try:
        students.status='F'
        students.user.is_active=0
        students.save()
        print('Disabled!')
        messages.success(request,'Student Disabled')
        return redirect('admin-view-student')
    except:
        print('Not Disable')
        messages.error(request,'Failed to Update')
        return redirect('admin-view-student')

@login_required   
def delete(request,id):
    student=Student.objects.get(id=id)
    try:
        student.delete()
        print('deleted Successfully!')
        messages.success(request,'Student Deleted')
        return redirect('admin-view-student')
    except:
        print('Not Deleted!')
        messages.error(request,'Failed to Delete!')
        return redirect('admin-view-student')

################# admin approve student ###############
@login_required
def adminApprovestudent(request):
    students=Student.objects.filter(status='F')
    context={
        'students' : students,
    }
    return render(request,'school/admin_approve_student.html',context)

@login_required      
def student_approve(request,id):
    students=Student.objects.get(id=id)
    try:
        students.status ='T'
        students.user.is_active = 1
        students.save()
        print('enabled Succcessfull!!')
        messages.success(request,'Student Enabled ')
        return redirect('admin-approve-student')
    except:
        print('Not enabled')
        messages.error(request,'Failed to Enable')
        return redirect('admin-approve-student')

@login_required   
def student_remove(request,id):
    students=Student.objects.get(id=id)
    try:
        students.status='F'
        students.user.is_active=0
        students.save()
        messages.success(request,'Student Disabled')
        print('Disabled!!')
        messages.error(request,'Failed to Disable')
        return redirect('admin-approve-student')
    except:
        print('Not')
        return redirect('admin-approve-student')


############### Admin view student fee ##############
@login_required
def adminViewStuFee(request):
    students = Student.objects.all()
    context={
        'students':students
    }
    return render(request,'school/admin_view_student_fee.html',context)

################### admin view attendance #################
@login_required
def adminattendence(request):
    return render(request,'school/admin_attendance.html')

@login_required
def adminAttendanceView(request,class1):
    if request.method == 'POST':
        form = AskDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            attendance = Attendence.objects.filter(date=date,class1=class1)
            students = Student.objects.filter(class1=class1)
            context={
                'class1':class1,
                'date':date,
                'attendance': attendance,
                'students':students,
            }
            return render(request,'school/admin_view_attendance_page.html', context)
        else:
            print(form.errors)
    else:
        form = AskDateForm()
        context={
            'class1':class1,
            'form':form
        }
        return render(request,'school/admin_view_attendance_ask_date.html',context)

################# admin view notice ###################
@login_required
def notice(request):
    form = NoticeForm()
    context={
        'form' : form,
    }
    return render(request,'school/admin_notice.html', context)

########################## Teacher ####################
@login_required
def teacherAttendence(request):
    return render(request,'school/teacher_attendance.html')

@login_required
def teacherTakeattendance(request,class1):
    students = Student.objects.filter(class1=class1)
    aform=AttendenceForm()
    if request.method == 'POST':
        form=AttendenceForm(request.POST)
        if form.is_valid():
            Attendences = form.cleaned_data['present_status']
            print('Attendances:', Attendences)
            date = form.cleaned_data['date']
            for i in range(len(Attendences)):
                user = Attendence()
                user.class1=class1
                user.date=date
                user.roll=students[i].roll
                user.present_status=Attendences
                print(user)
                user.save()
                messages.success(request,'Attendance Updated Successfully!!')
                return redirect('teacher-attendance')
        else:
            print(form.errors)
            messages.error(request,'Failed to Update!')
    
    context={
        'students':students,
        'aform':aform
    }
    return render(request,'school/teacher_take_attendance.html', context)


@login_required
def teacherAttendanceView(request,class1):
    if request.method == 'POST':
        form = AskDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            attendance = Attendence.objects.filter(date=date,class1=class1)
            print(attendance)
            students = Student.objects.filter(class1=class1)
            print(students)
            mylist=zip(attendance,students)
            context={
                'class1':class1,
                'date':date,
                'attendance': attendance,
                'students':students,
                'mylist':mylist
                
            }
            return render(request,'school/teacher_view_attendance_page.html', context)
        else:
            print(form.errors)
    else:
        form = AskDateForm()
        context={
            'class1':class1,
            'form':form
        }
        return render(request,'school/teacher_view_attendance_ask_date.html',context)

######################## student ######################
@login_required
def viewStudentAttendence(request):
    if request.method=='POST':
        form=AskDateForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data['date']
            students = Student.objects.filter(user_id = request.user.id)
            attendences = Attendence.objects.filter(date=date,
                                                    class1=students[0].class1,
                                                    roll = students[0].roll
                                                    )
            context={
                'date':date,
                'students':students,
                'attendences':attendences
            }
            return render(request,'school/student_view_attendance_page.html', context)
        else:
            print(form.errors)
    form=AskDateForm()
    return render(request,'school/student_view_attendance_ask_date.html',{'form':form})

## <-------------------- Code By ------------------------->
##<------------------ Md Ashif Haque ---------------------->