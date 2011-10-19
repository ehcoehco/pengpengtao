from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.comments import Comment

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    is_active = models.BooleanField(default=False)#is_active==True the user can login
    #weibo login
    #renren login
    
    def __unicode__(self):
        return "User id is :%s , User name is %s" %(self.id, self.user.username)

    def _get_name(self):
        return self.user.username

    def _set_name(self, name):
        self.user.username = name

    def __unicode__(self):
        return "%s user is %s"% (self.id, self.user.username)
    
    def get_absolute_url(self):
        return self.id# not finished
    
        

#RENREN User connection
class RENREN(models.Model):
    User = models.ForeignKey(User)
    RR_id = models.CharField(max_length=30, blank=True, db_index=True)#create index on this field
    RR_access_token = models.CharField(max_length=100, blank=True)
    RR_scope = models.CharField(max_length=20)
    RR_name = models.CharField(max_length=20, blank=True)



class Phone(models.Model):
    number = models.CharField(max_length=11)

    class Meta:
        verbose_name = "phone number"
        verbose_name_plural = "phone numbers"

    def _get_number(self):
        return number

    def _set_number(self, val):
        self.number = val


#for different types of deal
class DealType(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return self.content_type

class Discount(models.Model):
    discount = models.FloatField()
    deal_content = generic.GenericRelation(DealType)


class Gift(models.Model):
    gift = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)


class Deal(models.Model):
    content = models.ForeignKey(DealType)
    
    # add on part
    extension = models.CharField(max_length=140)

    
    begin_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    comments = models.ManyToManyField(Comment)

    def __unicode__(self):
        return self.id

    
    def get_absolute_url(self):
        return self.id# not finished

class UserDeal(models.Model):
    user = models.ForeignKey(User)
    deal = models.ForeignKey(Deal)
    STATE_CHOICE = ((0, 'Unused'),(1, 'Used'),(2, 'Invalid'))
    state = models.IntegerField(choices=STATE_CHOICE, max_length=1, default=0)


#business means  a merchant
class Merchant(models.Model):
    name = models.CharField(max_length=50)
    head_url = models.CharField(max_length=100)
    setupdate = models.DateField(default=datetime.now)
    introduce = models.TextField(blank=True, null=True)
    #login 
    user = models.OneToOneField(User, unique=True)
    username = models.CharField(max_length=50, unique=True)

    #a merchant have many deals
    deals = models.ManyToManyField(Deal, through='MerchantDeal')
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.id# not finished


class Invitation(models.Model):
    name = models.CharField(max_length=1)#temp
    #not determined
    def get_absolute_url(self):
        return self.id

#user phone connection #user has many phone 
class UserPhone(models.Model):
    user = models.ForeignKey(User)
    phone = models.ForeignKey(Phone)
    code = models.CharField(max_length=6)#no more than 6 char
    code_sendtime = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)#True means bounding the phone successfully or the false means not

#user get the deal can invite friends
class UserDealInvitation(models.Model):
    userdeal = models.ForeignKey(UserDeal)
    invitation = models.ForeignKey(Invitation)
    user = models.ForeignKey(User)
    is_agree = models.BooleanField(default=False)

#user's comment towards a deal
class UserDealComment(models.Model):
    user = models.ForeignKey(User)#in the comments there is a user part
    deal = models.ForeignKey(Deal)
    comments = models.ManyToManyField(Comment)#using the comment framework

#merchant pull the deal connection
class MerchantDeal(models.Model):
    merchant = models.ForeignKey(Merchant)
    deal = models.ForeignKey(Deal)
    

