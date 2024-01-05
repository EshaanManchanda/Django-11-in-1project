from django.shortcuts import redirect, render

# Create your views here.
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("account_login")
    context = {}
    return render(request, "pages/chatPage.html", context)