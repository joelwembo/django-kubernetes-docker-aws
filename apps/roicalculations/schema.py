from .models import Contact , RoiInvestment
from ninja import ModelSchema
class ContactBase(ModelSchema):
    class Config:
        model = Contact
        model_fields = ['first_name', 'last_name', 'organisation', 'phone_number']

# schema for contact creaton
class ContactCreate(ContactBase):
    pass


class Contact(ModelSchema):
    class Config:
        model = Contact
        model_fields = ['id','first_name', 'last_name','organisation', 'phone_number', 'created_on']

# Roi investment calculations

class InvestmentBase(ModelSchema):
    class Config:
        model = RoiInvestment
        model_fields = ['amount', 'totalinterest', 'ir', 'period', 'totalROIA', 'totalinvest', 'oneROIA', 'oneinterest']

# schema for contact creaton
class InvestmnetCreate(InvestmentBase):
    pass


class Investment(ModelSchema):
    class Config:
        model = Contact
        model_fields = ['amount', 'totalinterest', 'ir', 'period', 'totalROIA', 'totalinvest', 'oneROIA', 'oneinterest']
