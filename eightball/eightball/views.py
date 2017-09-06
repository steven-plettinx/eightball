from django.shortcuts import render

import string
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

randomanswer  = ""

def index(request):

    return render(request, '/views/index.html')

def answer(request):

    randomanswer = r.spop('answers')
    if randomanswer == None:
        r.sadd('answers', "It is certain")
        r.sadd('answers', "It is decidedly so")
        r.sadd('answers', "Without a doubt")
        r.sadd('answers', "Yes definitely")
        r.sadd('answers', "You may rely on it")
        r.sadd('answers', "As I see it, yes")
        r.sadd('answers', "Most likely")
        r.sadd('answers', "Outlook good")
        r.sadd('answers', "Yes")
        r.sadd('answers', "Reply hazy try again")
        r.sadd('answers', "Ask again later")
        r.sadd('answers', "Better not tell you now")
        r.sadd('answers', "Cannot predict now")
        r.sadd('answers', "Concentrate and ask again")
        r.sadd('answers', "Don't count on it")
        r.sadd('answers', "My reply is no")
        r.sadd('answers', "My sources say no")
        r.sadd('answers', "Outlook not so good")
        r.sadd('answers', "Very doubtful")
        randomanswer = r.spop('answers')

    return render(request, 'views/answer.html', {'answer': randomanswer})