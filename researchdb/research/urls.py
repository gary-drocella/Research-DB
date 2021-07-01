from django.urls import path
from django.views.generic import TemplateView

from research import views

app_name="research"

urlpatterns = [
    path('create_note', views.create_note_txt, name='create-note'),

    path('delete_note/<int:pk>', views.DeleteNote.as_view(), name='delete-note'),
    path('delete_note/success', TemplateView.as_view(template_name='delete_success.html'), name='delete-success'),

    path('edit_note/<int:pk>', views.EditNote.as_view(), name='edit-note'),
    path('edit_note/success', TemplateView.as_view(template_name='edit_success.html'), name='edit-success'),

    path('semesters', views.ListSemester.as_view(), name='list-semesters'),
    path('semester/<int:pk>', views.DetailSemester.as_view(), name='detail-semester'),

    path('courses', views.ListCourse.as_view(), name='list-courses'),
    path('course/<int:pk>', views.DetailCourse.as_view(), name='detail-course'),

    path('papers', views.ListPaper.as_view(), name='list-papers'),
    path('paper/<int:pk>', views.DetailPaper.as_view(), name='detail-paper'),

    path('', views.Index.as_view(), name='index')]