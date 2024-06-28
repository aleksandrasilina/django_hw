from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        with open('messages.txt', 'a') as file:
            file.write(f'{name}({email}): {message}\n')
    return render(request, 'contacts.html')
