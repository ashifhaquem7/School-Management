from django.urls import path
from . import views

urlpatterns = [

    #### Home urls #########
    path('',views.home),
    path('contactus/', views.contactUs, name='contactus'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),

    ##### login/signup ###########
    path('adminsignup/', views.adminSignup, name='adminsignup'),
    path('login/', views.login_view, name='login'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('forget_pass/', views.forget_password, name='forget_pass'),
    path('change_pass/<token>/', views.change_password, name='change_pass'),

    ##### teacher section ##############
    path('teachersignup/', views.teacherSignup, name='teachersignup'),
    path('teachersave/', views.teachersave, name='teachersave'),
    path('teacher-wait-for-approval', views.teacherwaitApproval,name='teacher-wait-for-approval'),
    path('teacher-attendance/', views.teacherAttendence, name='teacher-attendance'),
    path('teacher-take-attendance/<class1>', views.teacherTakeattendance, name='teacher-take-attendance'),
    path('teacher-attendance-view/<class1>', views.teacherAttendanceView, name='teacher-attendance-view'),
    
    ########### student section #######
    path('studentsignup/', views.studentSignup, name='studentsignup'),
    path('student_signup/', views.student_signup, name='student_signup'),
    path('student-wait-approval/', views.studentWaitApproval, name='student-wait-approval'),
    path('view-student-attendance/', views.viewStudentAttendence, name='view-student-attendance'),

    ########### Authentication ##############
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher-dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student-dashboard'),
    path('dologin',views.dologin, name='dologin'),
    path('logout-request', views.logout_request, name='logout-request'),

    ########### Full admin panel ############
    path('admin-teacher/',views.adminteacher, name='admin-teacher'),
    path('admin-add-teacher/', views.adminAddteacher, name='admin-add-teacher'),
    path('admin-add-teacher-view/', views.adminAddTeacher_view, name='admin-add-teacher-view'),
    path('edit-admin-teacher/<id>/', views.adminTeacher_edit, name='edit-admin-teacher'),
    path('edit_admin-tecaher-save', views.adminTeacher_save, name='edit-admin-teacher-save'),
    path('delete-teacher/<id>', views.deleteAdminTeacher, name='delete-teacher'),
    path('enable/<id>', views.adminTeacher_enable, name='enable'),
    path('disable/<id>', views.disable_adminTeacher, name='disable'),

    path('admin-student/', views.adminstudent, name='admin-student'),
    path('edit-admin-student/<id>', views.edit_adminStudent, name='edit-admin-student'),
    path('edit-admin-student-save', views.edit_adminStudent_save, name='edit-admin-student-save'),
    path('admin-attendence/', views.adminattendence, name='admin-attendence'),
    path('admin-view-attendance/<class1>', views.adminAttendanceView, name='admin-view-attendance'),
    path('admin-fee/', views.adminfee, name='admin-fee'),
    path('admin-view-fee/<class1>', views.adminViewFee, name='admin-view-fee'),
    path('admin-notice-view/', views.adminNotice_view, name='admin-notice-view'),

    path('admin-view-teacher/', views.adminVteacher, name='admin-view-teacher'),
    path('admin-add-teacher/', views.adminAddteacher, name='admin-add-teacher'),
    path('admin-approve-teacher/', views.adminApproveteacher, name='admin-approve-teacher'),
    path('approve-teacher/<id>', views.teacher_approve, name='approve-teacher'),
    path('remove-teacher/<id>', views.teacher_remove, name='remove-teacher'),
    path('admin-view-teacher-salary/', views.adminViewTechSalary, name='admin-view-teacher-salary'),

    path('admin-view-student/', views.adminVstudent, name='admin-view-student'),
    path('admin-add-student/', views.adminAddstudent, name='admin-add-student'),
    path('admin-add-student-view/',views.adminAddStudent_view, name='admin-add-student-view'),
    path('enable_student/<id>', views.enable_adminStudent, name='enable_student'),
    path('disable_student/<id>', views.disable_adminStudent, name='disable_student'),
    path('delete_student/<id>', views.delete, name='delete_student'),
    path('admin-approve-student/', views.adminApprovestudent, name='admin-approve-student'),
    path('approve-student/<id>', views.student_approve, name='approve-student'),
    path('remove-student/<id>', views.student_remove, name='remove-student'),
    path('admin-view-student-fee/', views.adminViewStuFee, name='admin-view-student-fee'),

    ########## Admin Notice ###########
    path('notice/', views.notice, name='notice'),

    ### code by #####
    #### Md Ashif Haque ########
    
    
    

    


]