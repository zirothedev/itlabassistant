from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
import calendar
import datetime
from .models import CalendarEntry
from .forms import CalendarEntryForm

class CalendarView(generic.ListView):
    model = CalendarEntry
    template_name = 'calendar_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get year and month from URL parameters or use current date
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)
        return context

    def get_date(self, req_month):
        if req_month:
            year, month = (int(x) for x in req_month.split('-'))
            return datetime.date(year, month, day=1)
        return datetime.date.today()

    def prev_month(self, d):
        first = d.replace(day=1)
        prev_month = first - datetime.timedelta(days=1)
        month = f'{prev_month.year}-{prev_month.month}'
        return month

    def next_month(self, d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + datetime.timedelta(days=1)
        month = f'{next_month.year}-{next_month.month}'
        return month

class Calendar(calendar.HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super().__init__()

    def formatday(self, day, weekday):
        if day != 0:
            date = datetime.date(self.year, self.month, day)
            entries = CalendarEntry.objects.filter(date=date)
            d = ''
            for entry in entries:
                completed_class = 'completed' if entry.completed and entry.entry_type == 'TODO' else ''
                type_class = entry.entry_type.lower()
                d += f'<li class="{type_class} {completed_class}" data-id="{entry.id}">{entry.title}</li>'
            
            return f"<td class='day'><span class='date'>{day}</span><ul>{d}</ul><a class='add-entry' href='{reverse_lazy('calendar_app:entry_new')}?date={date}'>+</a></td>"
        return "<td class='day other-month'></td>"

    def formatweek(self, theweek):
        week = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear=True):
        cal = f'<table class="calendar">\n'
        cal += f'<caption class="month-header">{calendar.month_name[self.month]} {self.year}</caption>\n'
        cal += f'<tr class="weekdays">{self.formatweekheader()}</tr>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week)}\n'
        cal += f'</table>'
        return cal

class EntryCreate(generic.CreateView):
    model = CalendarEntry
    form_class = CalendarEntryForm
    template_name = 'calendar_app/entry_form.html'
    
    def get_initial(self):
        initial = super().get_initial()
        if 'date' in self.request.GET:
            initial['date'] = self.request.GET.get('date')
        return initial

class EntryDetail(generic.DetailView):
    model = CalendarEntry
    template_name = 'calendar_app/entry_detail.html'

class EntryUpdate(generic.UpdateView):
    model = CalendarEntry
    form_class = CalendarEntryForm
    template_name = 'calendar_app/entry_form.html'

class EntryDelete(generic.DeleteView):
    model = CalendarEntry
    template_name = 'calendar_app/entry_confirm_delete.html'
    success_url = reverse_lazy('calendar_app:calendar')

def toggle_completed(request, pk):
    entry = get_object_or_404(CalendarEntry, pk=pk)
    entry.completed = not entry.completed
    entry.save()
    return redirect('calendar_app:calendar')

