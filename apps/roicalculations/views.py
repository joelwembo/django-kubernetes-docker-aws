from django.shortcuts import render
import sys
import datetime as date
from datetime import *
from .models import Contact as contact_table , RoiInvestment



# Create your views here.
def home(request):
    return render(request, 'home.html')


def goToHome(request):
    return render(request, 'home.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')


def index(request):
    return render(request, 'index.html')


def renderresult(request):
    return render(request, 'renderresult.html')


def schemes(request):
    return render(request, 'schemes.html')


def passdata(request):
    x = int(request.GET['amount'])
    y = int(request.GET['period'])
    context = {'amount': x, 'period': y}
    return render(request, 'schemes.html', context)


def gold(request, amount, duration):
    ir = 30
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest,'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


def ppf(request, amount, duration):
    ir = 8
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


def nsc(request, amount, duration):
    ir = 7
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


def fd(request, amount, duration):
    ir = 6
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


def elss(request, amount, duration):
    ir = 15
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


def emf(request, amount, duration):
    ir = 13
    investamount = amount
    investAmount = []
    ROIAmount = []
    InterstAmount = []
    for i in range(duration):  # 10
        investAmount.append(amount)
        x = amount * ir / 100
        InterstAmount.append(x)
        amount = amount + x
        ROIAmount.append(amount)
    oneinterest = InterstAmount[0]
    oneROIA = ROIAmount[0]
    totalinterest = sum(InterstAmount)
    totalROIA = sum(ROIAmount)
    totalinvest = sum(investAmount)
    context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}
    return render(request, 'renderresult.html', context)


class Contact:
    def __init__(self):
        pass

    def create_contact(request, contact):
        try:
            if type(contact) != "dict":
                contact = contact.dict()
            contact = contact_table.objects.create(**contact)
            contact.save()
            if contact:
                return "contact saved"
            return {"error ": "failed to save"}
        except Exception as error:
            return str(error)

    def get_contacts(request):
        try:
            contacts = contact_table.objects.all()
            return contacts
            if contacts:
                return contacts
            return {status: 500, context: "failed to save"}
        except Exception as error:
            return str(error)

#  Class for invesmtne roi calculation
class ROIInvestmnet:
    def __init__(self):
        pass

    def create_investment(request, RoiInvestment):
        try:
            if type(RoiInvestment) != "dict":
                RoiInvestment = RoiInvestment.dict()
            RoiInvestment = RoiInvestment.objects.create(**RoiInvestment)
            RoiInvestment.save()
            if RoiInvestment:
                return "Invesment Saved saved"
            return {"error ": "failed to save"}
        except Exception as error:
            return str(error)

    def get_investment(request):
        try:
            investment = RoiInvestment.objects.all()
            return investment
            if investment:
                return investment
            return {status: 500, context: "failed to save"}
        except Exception as error:
            return str(error)