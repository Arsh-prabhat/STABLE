from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def survey_view(request):
    # Example list of questions fetched from a database or defined in Python
    
    questions = [
    {
        'text': "I feel overwhelmed by emotions",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I have physical symptoms of anxiety, such as sweaty palms",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I find it hard to concentrate on tasks",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I am able to handle the level of stress I experience.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I have strong relationships with people I care about.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I've made many terrible decisions in my life.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I am very self-critical.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I cannot get beyond long-past traumatic events or significant losses.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I am able to identify and express my emotions.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I trust that if I confide in others, they will be supportive.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I engage in at least one behavior that significantly impairs my ability to function on a daily basis",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "When I experience a strong emotion, I usually know why it's hitting me.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "My mood is stable.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I procrastinate and/or avoid dealing with important things in my life.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I often feel sad.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I have a sense of purpose in life.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I often feel lonely.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I get upset or angry easily.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I've noticed changes in my appetite or sleep patterns relative to when I was at my best.",
        'option_1_value': 5,
        'option_2_value': 4,
        'option_3_value': 3,
        'option_4_value': 2,
        'option_5_value': 1
    },
    {
        'text': "I'm able to bounce back from setbacks.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    },
    {
        'text': "I manage my time and my obligations; most days life feels under control.",
        'option_1_value': 1,
        'option_2_value': 2,
        'option_3_value': 3,
        'option_4_value': 4,
        'option_5_value': 5
    }
]

    if request.method == 'POST':
        answers = []

        for i in range(1, len(questions) + 1):  
            answer = request.POST.get(f'q{i}')
            if answer is None:
                return HttpResponse(f"Error: Please answer question {i}.")
            answers.append(int(answer))

        # Calculate the score based on answers
        score = (sum(answers) / len(answers)) * 10

        # Determine the result based on the score
        if score <= 30:
            result = "You may be facing some challenges. Consider talking to a professional."
        elif score <= 50:
            result = "You do not seem to be doing okay but could use some positive coping strategies."
        elif score <= 70:
            result = "You seem to be doing okay but could use some positive coping strategies."
        else:
            result = "You appear to be in a good mental state. Keep it up!"

        # Redirect to the result page
        return render(request, 'result.html', {'score': score , 'result': result})

    return render(request, 'survey.html', {'questions': questions})

def home(request):
    return render (request, "home.html")

def surveyhome(request):
    return render (request, "startsurvey.html")

def card1(request):
    return render (request, "card1.html")

def card2(request):
    return render (request, "card2.html")

def card3(request):
    return render (request, "card3.html")

def card4(request):
    return render (request, "card4.html")

def signup_view(request):
    if request.method == 'POST':
        Firstname= request.POST['Firstname']
        Lastname= request.POST['Lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        else:
            user = User.objects.create_user( Firstname=Firstname, Lastname=Lastname,username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')  # Redirect to home or dashboard after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Stay on login page if credentials are wrong

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def chatbot_view(request):
    return render(request, 'chatbot.html')
@login_required
def user_details(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'details.html', {'user': user})

def wellness(request):
    return render(request, 'wellness.html')

def low(request):
    return render(request, 'r1.html')