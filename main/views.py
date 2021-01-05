from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tasks, fight_tab, user_stats
from .forms import TaskForm, fight_tab_form, user_statts


def index(request):
    taksk = Tasks.objects.all()
    return render(request, 'main/index.html', {'title': 'main_page_site', 'task1': taksk })


def forum(request):
    return render(request, 'main/forum.html')


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            error = 'Not enough data'
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/create_task.html', context)


def calculator_def(request):
    return render(request, 'main/calculator.html')

# Показываем ту же страницу но с изменениями
def submit_query(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydic = {
            'q': q,
            'ans': ans,
            'error': False,
            'result': True
        }
        return render(request,'main/calculator.html', context=mydic)
    except:
        mydic = {
            'error': True,
            'result': False
        }
        return render(request,'main/calculator.html', context=mydic)

def fighting_page(request):
    your_name = 'try_me'
    my_dict = {
        'your_name_irl': your_name,
    }
    return render(request,'main/fight.html', my_dict)

def fighting_page_form(request):
    if request.method == "POST":
        my_new_title = request.POST.get('yours')
        print(my_new_title)
    context = {}
    return render(request,'main/fight_create.html', context)


# def user_stattts(request):
#     if request.method == 'POST':
#         form_ = user_statts(request.POST)
#         if form_.is_valid():
#             form_.save()
#             HttpResponse(form_)
#         else:
#             pass


def user_stattts(request):
    errror = ''
    if request.method == 'POST':
        form = user_statts(request.POST)
        if form.is_valid():
            form.save()
            form = user_statts
        else:
            errror = 'not enough data'
    form = user_statts()
    context = {'form': form}
    return render(request, 'main/userstat.html', context)
# def fighting_page_form(request):
#     form = fight_tab_form(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = fight_tab_form()
#     context = {
#         'form': form
#     }
#     return render(request,'main/fight_create.html', context)

