from django.views.generic import TemplateView,View,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Book 
from .forms import BookForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class HomeView(TemplateView):
    template_name = 'book/home.html'


class BookCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form=BookForm()
        return render(request,'book/book_form.html',{'form':form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            books=form.save(commit=False) #make instance here
            books.user=request.user 
            books.save()
            messages.success(request,"Book Created Successfully")
            return redirect('book-list')
        return render(request,'book/book_form.html',{'form':form})
    

class BookListView(LoginRequiredMixin,TemplateView):
    template_name='book/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Only show books created by current user
        context['books'] = Book.objects.filter(user=self.request.user)
        return context

class BookDetailView(DetailView):
    model=Book
    template_name='book/book_detail.html'

    def get_queryset(self):
         # Restrict access so a user only sees their own books
        return Book.objects.filter(user=self.request.user)
class BookUpdateView(UpdateView):
    # The model we're updating
    model=Book
    fields=['title','author','genre','description']
    # Template for the update form
    template_name='book/book_form.html'
    # Redirect after successful update
    success_url=reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, "Book updated successfully")
        return super().form_valid(form)
    

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model=Book
    template_name='book/book_confirm_delete.html'
    success_url=reverse_lazy('book-list')

    def get_queryset(self):
         # Restrict deletion to books owned by the current user
        return Book.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Book deleted successfully")
        return super().delete(request, *args, **kwargs)