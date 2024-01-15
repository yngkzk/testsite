from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import IceCream, IceCreamKiosk, Comment, Task


def home_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def test_site(request):
    ice_creams = IceCream.objects.order_by('calories')
    ice_cream_kiosks = IceCreamKiosk.objects.all()
    context = {'ice_creams': ice_creams, 'ice_cream_kiosks': ice_cream_kiosks}
    return render(request, 'testsite.html', context)


def sms_view(request):
    messages = Comment.objects.all()
    return render(request, 'smsview.html', {'messages': messages})


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "adminlogin" and password == "aabbddaa123":  # Сделать так, чтобы он искал в файле, если нету, то
            with open('txt_db/login', 'r+', encoding='utf-8') as file:  # Добавлял нового
                file.write(f'{username}={password}')
        else:
            return HttpResponseRedirect('about')

    return render(request, 'login.html')


class TaskController:

    @staticmethod
    def get_task(request, task_id):
        task = Task.objects.filter(id=task_id).first()
        if not task:
            return JsonResponse({"error": "Task not found"})

        data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
        }
        return JsonResponse(data)

    @staticmethod
    def get_all_tasks(request):
        tasks = Task.objects.all()
        data = [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at,
                "updated_at": task.updated_at,
            }
            for task in tasks
        ]
        return JsonResponse(data)

    @staticmethod
    def add_task(request, title, description):
        task = Task(title=title, description=description)
        task.save()

        data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
        }
        return JsonResponse(data)

    @staticmethod
    def delete_task(request, task_id):
        task = Task.objects.filter(id=task_id).first()
        if not task:
            return JsonResponse({"error": "Task not found"})

        task.delete()

        return JsonResponse({"success": True})
