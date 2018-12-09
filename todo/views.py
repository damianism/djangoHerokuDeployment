from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def say_hello(request):
    return HttpResponse("Hellow World")
    
def get_test(request):
    return render(request, "test.html")

def get_todo_list(request):
    results = Item.objects.all()
    # for x in results:
    #     print(x.name, x.done)
    return render(request, "todo_list.html", {"items": results})

# def create_an_item(request):
    
#     if request.method == "POST":
#         print(request.POST) 
#         new_item = Item()  # intance of the Item class created in models "EMPTY!"
#         new_item.name = request.POST.get("name")    # fetch from form
#         new_item.done = "done" in request.POST      # saves a true or false value in the database
#         new_item.save()
#         return redirect(get_todo_list)
        
#     return render(request, "item_form.html")


def create_an_item(request):
    
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()
        
    return render(request, "item_form.html", {'form':form})
    

def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id) # pk being the Primary Key
    
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form':form})
    
    
def toggle_an_item(request, id):
    item = get_object_or_404(Item, pk=id) # pk being the Primary Key
    
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)

    
    