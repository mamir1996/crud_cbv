from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.views.generic.edit import UpdateView
from .models import Book 
from .forms import BookForm

class HomeView(TemplateView):
    template_name='book/home.html'

#create

class BookCreateView(TemplateView):
    def get(self,request):
        form=BookForm()
        return render(request,'book/book_form.html',{'form':form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        messages.success(request,"Book created successfully")
        return render(request,'book/book_form.html',{'form':form})

# Read /view 
class BookListView(TemplateView):
    template_name='book/book_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['books']=Book.objects.all()
        return context
#detail
class BookDetailView(TemplateView):
    template_name='book/book_detail.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        book=get_object_or_404(Book,id=kwargs['pk'])
        context['book']=book 
        return context 
#edit 
class BookUpdateView(UpdateView):
    model=Book #Tells the view which model to update
    # form=BookForm #Reuses the same form used for creating a book
    fields = ['title', 'author', 'description']
    template_name='book/book_form.html' #ses the same form template
    success_url='/books/'  	#After updating, redirect back to book list
#delete
class BookDeleteView(View):
    def get(self,request,pk):
        book=get_object_or_404(Book,id=pk)
        book.delete()
        return redirect('book-list')