from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ielts_db import views
from rest_framework import permissions
# from django.conf.urls import url


schema_view = get_schema_view(
    openapi.Info(
        title="IELTS API docs",
        default_version='v0.1',
        description="Test API docs",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        #license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'certificate', views.CertificateViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'essayquestion', views.EssayquestionViewSet)
router.register(r'exam', views.ExamViewSet)
router.register(r'subquestion', views.SubquestionViewSet)
router.register(r'reportperlesson', views.ReportperlessonViewSet)

# router.register(r'students', views.StudentViewSet,basename="students")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='user-register'),
    re_path(r'^login/$', views.LoginView.as_view(), name='user-login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='user-logout'),
    re_path(r'^current/$', views.UserView.as_view(), name='user-current'),
    re_path(r'^change-password/$', views.ChangePasswordView.as_view(), name='change-password'),
]
