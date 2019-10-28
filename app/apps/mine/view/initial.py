from django.shortcuts import redirect, render, reverse


def initial(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='miner').exists():
            beginner_classroom_pk = 25
            return redirect(reverse('mine:miner-tasks', kwargs={'pk': beginner_classroom_pk}))
        else:
            return redirect('mine:moderator-initial')
    return render(request, 'authentication/initial.html')


def error404(request, exception):
    return render(request, 'mine/404.html', status=404)


def error500(request):
    return render(request, 'mine/500.html', status=500)