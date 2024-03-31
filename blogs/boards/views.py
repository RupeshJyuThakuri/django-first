from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
# def home(request):
#     boards = Board.objects.all()
#     boards_name = []
    
#     for board in boards:
#         boards_name.append(board.subject)
    
#     response_html ='<br>'.join(boards_name)
    
#     return HttpResponse(response_html)

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})



def course(request):
    return HttpResponse('Hello! This is course section')

def courseDetails(request, courseid):
    return HttpResponse(courseid)

