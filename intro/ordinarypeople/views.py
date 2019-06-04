from django.shortcuts import render
import random
import math
from datetime import datetime
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'ordinarypeople/index.html')