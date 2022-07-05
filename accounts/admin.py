from django.contrib import admin
from voting.models import *

# Register your models here.
admin.site.register(Voter)
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Votes)