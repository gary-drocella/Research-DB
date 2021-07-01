from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponse

from research.models import Note, Semester, Course, Paper
from research.forms import NoteForm

# Create your views here.

class CreateNote(CreateView):
    model = Note
    fields = '__all__'

class DeleteNote(DeleteView):
    model = Note
    fields = '__all__'

    def get_success_url(self):
        return reverse('research:delete-success')
    
    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['txt'] = self.object.txt
        return context

class EditNote(UpdateView):
    model = Note
    fields = '__all__'

    def get_success_url(self):
        return reverse('research:edit-success')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['note'] = self.object
        return context        

class ListSemester(ListView):
    model = Semester
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['semesters'] = Semester.objects.all()
        return context

class ListCourse(ListView):
    model = Course
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

class ListPaper(ListView):
    model = Paper
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['papers'] = Paper.objects.all()
        return context

class DetailSemester(DetailView):
    model = Semester
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        qs = Semester.objects.filter(id=self.object.id)

        try:
            context['semester'] = qs[0]
        except IndexError:
            context['semester'] = None
        
        return context

class DetailCourse(DetailView):
    model = Course
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        qs = Course.objects.filter(id=self.object.id)

        try:
            context['course'] = qs[0]
        except IndexError:
            context['course'] = None
        
        return context

class DetailPaper(DetailView):
    model = Paper
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        qs = Paper.objects.filter(id=self.object.id)

        try:
            context['paper'] = qs[0]
        except IndexError:
            context['paper'] = None
        
        return context

def create_note_txt(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            qs = Paper.objects.filter(id=form.cleaned_data["paper_id"])
            paper = qs[0]
            note = Note(txt=form.cleaned_data["note_txt"])
            note.save()
            paper.notes.add(note)
            paper.save()

            return redirect(reverse('research:detail-paper', args=[form.cleaned_data["paper_id"]]))
        else:
            return render(request, "error.html", {'error_msg_header': 'Could Not Create Note', 'error_msg': 'The note is empty.'})
    

    return render(request, reverse('research:detail-paper'), {'form': NoteForm()})

class Index(TemplateView):
    template_name = 'research/index.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['semester_count'] = Semester.objects.all().count()
        context['course_count'] = Course.objects.all().count()
        context['paper_count'] = Paper.objects.all().count()

        return context
