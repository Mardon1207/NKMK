from django.shortcuts import render
from .models import Spravochniks
from django.db.models import Q
import math
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.management.commands import makemessages
from django.utils.translation import gettext as _

class Command(makemessages.Command):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--extra-keyword', dest='xgettext_keywords',
                            action='append')

    def handle(self, *args, **options):
        xgettext_keywords = options.pop('xgettext_keywords')
        if xgettext_keywords:
            self.xgettext_options = (
                makemessages.Command.xgettext_options[:] +
                ['--keyword=%s' % kwd for kwd in xgettext_keywords]
            )
        super(Command, self).handle(*args, **options)
# Create your views here.
def telefon(request):
    page_number = int(request.GET.get('page', 1))
    entries = int(request.GET.get('entries', 50))
    
    
    search_key = request.GET.get('search', '')
    filter_options = Q(
        FullName__icontains=search_key
    ) | Q(
        Branch__name__icontains=search_key
    ) | Q(
        Department__name__icontains=search_key
    ) | Q(
        Positions__name__icontains=search_key
    ) | Q(
        Stationary__icontains=search_key
    ) | Q(
        Mobile__icontains=search_key
    )
    all_data = Spravochniks.objects.filter(filter_options)
    total_entries = all_data.count()
    total_pages = math.ceil(total_entries / entries)
    data = [
        [
            
            getattr(spravochnik, 'FullName'),
            getattr(spravochnik, 'Branch').name if getattr(spravochnik, 'Branch') else '',
            getattr(spravochnik, 'Department').name if getattr(spravochnik, 'Department') else '',
            getattr(spravochnik, 'Positions').name if getattr(spravochnik, 'Positions') else '',
            getattr(spravochnik, 'Stationary'),
            getattr(spravochnik, 'Mobile'),
            
        ]
        for spravochnik in all_data[(page_number-1)*entries : page_number*entries]
    ]

    return render(request, 'telefon.html', context={
        'data': data,
        'total_pages': range(1, total_pages + 1),
        'has_prev': page_number > 1,
        'has_next': page_number < total_pages,
        'current_page': page_number,
        'entries': entries,
        'search': search_key,
    })

def index(request):
    return render(request, 'index.html')


def telefonadmin(request):
    page_number = int(request.GET.get('page', 1))
    entries = int(request.GET.get('entries', 50))
    
    
    search_key = request.GET.get('search', '')
    filter_options = Q(
        FullName__icontains=search_key
    ) | Q(
        Branch__name__icontains=search_key
    ) | Q(
        Department__name__icontains=search_key
    ) | Q(
        Positions__name__icontains=search_key
    ) | Q(
        Stationary__icontains=search_key
    ) | Q(
        Mobile__icontains=search_key
    ) | Q(
        creator__icontains=search_key
    ) | Q(
        created__icontains=search_key
    ) | Q(
        changer__icontains=search_key
    ) | Q(
        changed__icontains=search_key
    )
    all_data = Spravochniks.objects.filter(filter_options)
    total_entries = all_data.count()
    total_pages = math.ceil(total_entries / entries)
    data = [
        [
            
            getattr(spravochnik, 'FullName'),
            getattr(spravochnik, 'Branch').name if getattr(spravochnik, 'Branch') else '',
            getattr(spravochnik, 'Department').name if getattr(spravochnik, 'Department') else '',
            getattr(spravochnik, 'Positions').name if getattr(spravochnik, 'Positions') else '',
            getattr(spravochnik, 'Stationary'),
            getattr(spravochnik, 'Mobile'),
            getattr(spravochnik, 'creator'),
            getattr(spravochnik, 'created'),
            getattr(spravochnik, 'changer'),
            getattr(spravochnik, 'changed'),
            
        ]
        for spravochnik in all_data[(page_number-1)*entries : page_number*entries]
    ]

    return render(request, 'telefonadmin.html', context={
        'data': data,
        'total_pages': range(1, total_pages + 1),
        'has_prev': page_number > 1,
        'has_next': page_number < total_pages,
        'current_page': page_number,
        'entries': entries,
        'search': search_key,
    })


# def yangiliklar(request):
#     return render(request, 'yangiliklar.html')

# def yangiliklaradmin(request):
#     return render(request, 'yangilikadmin.html')

def eroror(request):
    return render(request, '404error.html')