from datetime import datetime, timedelta, time
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from sleeptracker.models import SleepState

import json

def timeslices(start, end, t):
    split = datetime(start.year, start.month, start.day, 
                     t.hour, t.minute, t.second)

    if split <= start:
        split += timedelta(days=1)

    ss = split - start
    es = end - start
    
    if es <= ss:
        return [(start, end)]
    else:
        return [(start, split)] + timeslices(split, end, t)

def x(d, t, c):
    return c - (t-d).days + 1

def y(dt, t):
    offset = t.hour * 60 + t.minute
    ms = dt.minute + dt.hour * 60
    result = ms - offset
    if result < 0:
        return result + 1440
    else:
        return result

def z(dt, t):
    offset = t.hour * 60 + t.minute
    ms = dt.minute + dt.hour * 60
    result = ms - offset
    if result <= 0:
        return result + 1440
    else:
        return result

def yaxis(t):
    hour = t.hour
    return dict((1440 - a * 180, "%s:%02d" % ((hour + a * 3) % 24, t.minute)) for a in range(0, 9))


class UserView(DetailView):

    context_object_name = "user"
    template_name = "sleeptracker/user_detail.html"
    model = User

    def get_object(self):
        username = self.kwargs["username"]
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        data = SleepState.objects.filter(user=self.object, state=1)
        t = time(int(self.request.GET.get("hour", 15)))
        slices = []
        for ss in data:
            slices += timeslices(ss.start, ss.end, t)
        l = slices[:1][0][0]
        f = slices[-1:][0][0]
        c = (l - f).days
        proto = [ {"x": x(s[0], l, c), "y": y(s[0], t), "z": z(s[1], t), "data": str(s[0])} for s in slices]
        
        context["data"] = json.dumps(proto)
        context["count"] = c
        context["yaxis"] = yaxis(t)
        if len(data):
            context['cstate'] = data[0]
        return context
