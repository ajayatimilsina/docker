from django.shortcuts import render
from .forms import StudentRegistrationForm  # Correct import statement

def index(request):
    form = StudentRegistrationForm()
    # Render a page with the form
    return render(request, 'formapp/index.html', {'form': form})
