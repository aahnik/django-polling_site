"""
NOTE
SEE README FOR DETAILS ABOUT RUNNING THIS PYTHON SCRIPT

 """


from django.utils import timezone

# run from manage.py shell otherwise you will face error
from poll.models import Question, Choice

import random
import string
import datetime


def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_para(lim_char):
    para = ""
    count = 0
    while count <= lim_char:
        i = random.randint(3, 8)
        count += i
        word = random_string(i)
        para = para + " " + word
    if len(para) > lim_char:
        para = para[:lim_char]
    return para.strip()


for i in range(30):
    title = random_para(50)
    desc = random_para(200)
    pub_date = timezone.now() - datetime.timedelta(days=random.randint(0, 10))
    featured = True if i % 2 == 0 else False

    q = Question(title=title, desc=desc,
                 pub_date=pub_date, featured=featured)
    q.save()

    for j in range(4):
        choice_text = random_para(100)
        votes = random.randint(0, 8)
        c = q.choice_set.create(choice_text=choice_text, votes=votes)
