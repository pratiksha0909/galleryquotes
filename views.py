from django.shortcuts import render
def home(request):
    return render(request,'temp/index.html')
def show(request):
    msg="Hey user good mornnig!!! have a great day"
    mydata={'msg':msg}
    type='home'
    return render(request,'temp/home.html',mydata)
def quotes(request):
    speakers = [
        {
            'name': '1. Dave Ramsey',
            'about': 'David Ramsey is an American financial author, radio host, television personality, and motivational speaker. His show and writings strongly focus on encouraging people to get out of debt.',
            'website': 'https://ashiqspeaks.com',
            'twitter': '@ashiq_speaks',
            'facebook': 'facebook.com/ashiqspeaks',
            'popularity': '5 Million Followers',
            'images':"images/m5.jpg"
            
        },
        {
            'name': '3. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m2.jpg"

        },
         {
            'name': '3. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m3.jpg"

        },
         {
            'name': '4. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m4.jpg"

        },
         {
            'name': '5. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m5.jpg"

        },
         {
            'name': '6. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m6.jpg"

        },
         {
            'name': '7. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m7.jpg"

        },
         {
            'name': '8. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/m5.jpg"

        },
         {
            'name': '9. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/Dr.jpg"

        },
         {
            'name': '10. Tony Robbins',
            'about': 'Tony Robbins is an American author, coach, speaker, and philanthropist.',
            'website': 'https://tonyrobbins.com',
            'twitter': '@tonyrobbins',
            'facebook': 'facebook.com/tonyrobbins',
            'popularity': '10 Million Followers',
            'images':"images/Dr.jpg"

        },
    ]
    context = {
        'speakers': speakers,
        'type': 'quotes',  # Ensure 'type' is included
    }
    return render(request, 'temp/home.html', context)

   

def abou(request):
    msg="Hey user good mornnig!!! have a great day"
    mydata={'msg':msg}
    type='about'
    return render(request,'temp/home.html',mydata)
def your(request):
    msg="Hey user good mornnig!!! have a great day"
    mydata={'msg':msg}
    type='yourquotes'
    return render(request,'temp/home.html',mydata)