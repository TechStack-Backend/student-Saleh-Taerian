from django.shortcuts import render, HttpResponse
developers = [
    {
        "username": "hassan",
        "firstname": "Hassan",
        "last_name": "kabirian",
        "skills": ["Python", "Django", "Vue.js"],
    },
    {
        "username": "sara",
        "firstname": "Sara",
        "last_name": "Ahmadi",
        "skills": ["JavaScript", "React", "CSS"],
    },
    {
        "username": "ali",
        "firstname": "Ali",
        "last_name": "Rezayi",
        "skills": ["Java", "Spring Boot" , "SQL"],
    },
     ]
def show_users(request):
    return render(request , "devListApp/devlist.html" , {"devDict":developers})
def show_cv(request , username):
   for dev in developers:
        if dev["username"]==username:  
          return render(request , "devListApp/cv.html" , {"pointedDev":dev})
   return HttpResponse("<h1>user not found!</h1>")