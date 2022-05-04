from math import degrees
import profile
from pyexpat import model
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

from django.forms import DateField
from .choices import *
from datetime import timedelta
from datetime import datetime as dt
from tutorial.models import TutorModel
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

today = datetime.date.today()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    phonenumber = models.IntegerField(blank=False)
    address = models.CharField(max_length=500, blank=False, default=False)
    profilepix = models.FileField(default=0, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class Class(models.Model):
    classes = models.CharField(max_length=100, choices=CLASSES_CHOICES)

    def __str__(self):
        return self.classes


class Subject(models.Model):
    subjects = models.CharField(max_length=300, choices=SUBJECTS_CHOICES)

    def __str__(self):
        return self.subjects


class Location(models.Model):
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.location


class Becometutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    whatsappnumber = models.IntegerField(blank=False)
    dob = models.DateField(auto_created=True, null=False)
    sex = models.CharField(
        max_length=20, choices=SEX_CHOICES, default='Not Sure')
    address = models.TextField(max_length=500)
    primarylanguage = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    teachinglocations = models.ManyToManyField(Location)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Educationalhistory(models.Model):
    tutor = models.ForeignKey(
        Becometutor, on_delete=models.CASCADE, default=None)
    school = models.CharField(max_length=800)
    country = models.CharField(max_length=300)
    start = models.DateField(auto_created=True, null=False)
    end = models.DateField(auto_created=True, null=False)
    course = models.CharField(max_length=500)
    degrees = models.CharField(max_length=500)
    grade = models.CharField(max_length=300)

    def __str__(self):
        return self.tutor.email


class Workhistory(models.Model):
    tutor = models.ForeignKey(
        Becometutor, on_delete=models.CASCADE, default=None)
    organization = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    dob = models.DateField(auto_created=True, null=False)
    dob = models.DateField(auto_created=True, null=False)
    roll = models.CharField(max_length=300)
    active = models.BooleanField()

    def __str__(self):
        return self.tutor.email


class Gettutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    kidsnum = models.CharField(max_length=50)
    classofkid = models.ManyToManyField(Class)
    modeoftutor = models.CharField(
        max_length=20, choices=MODE_CHOICES, default='Not Sure')
    goalofchild = models.CharField(
        max_length=100, choices=GOALS_CHOICES)
    subjects = models.ManyToManyField(Subject)
    briefbio = models.TextField(max_length=3000)
    curiculum = models.CharField(
        max_length=100, choices=CURICULUM_CHOICES, default='Not Sure')
    typeoftutor = models.CharField(
        max_length=20, choices=SEX_CHOICES, default='Not Sure')
    address = models.TextField(max_length=500)
    state = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=14)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    Start = models.DateField(auto_created=True, null=False)
    hrsperday = models.CharField(
        max_length=10, choices=HOURS_CHOICES, default='Not Sure')
    starttime = models.CharField(
        max_length=500, choices=START_TIME_CHOICES, default="Not Sure")
    timestamp = models.DateTimeField(auto_now=True)
    duration = models.PositiveBigIntegerField(
        default=1, choices=DURATION_CHOICES)

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=Gettutor)
def payment_ammount(sender, instance, *args, **kwargs):
    if instance.duration == 1:
        Activetutor.objects.create(turorialkey=instance, amount=1600.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))
    elif instance.duration == 7:
        Activetutor.objects.create(turorialkey=instance, amount=11200.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))
    elif instance.duration == 30:
        Activetutor.objects.create(turorialkey=instance, amount=48000.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))
    elif instance.duration == 90:
        Activetutor.objects.create(turorialkey=instance, amount=144000.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))
    elif instance.duration == 180:
        Activetutor.objects.create(turorialkey=instance, amount=288000.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))
    else:
        Activetutor.objects.create(turorialkey=instance, amount=1600.00,
                                   expires_in=instance.Start + timedelta(days=instance.duration))


class Activetutor(models.Model):
    turorialkey = models.ForeignKey(
        Gettutor, related_name='status', on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    expires_in = models.DateField(null=True, auto_created=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.turorialkey.user.username


@ receiver(post_save, sender=Activetutor)
def expiring_date(sender, instance, *args, **kwargs):
    if instance.expires_in == today:
        turorialkey = Activetutor.objects.get(id=instance.id)
        turorialkey.delete()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    referenceCode = models.CharField(max_length=100, default='', blank=True)
    paystackAccessCode = models.CharField(
        max_length=100, default='', blank=True)
    paymentFor = models.ForeignKey(
        TutorModel, on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    duration = models.PositiveBigIntegerField(default=30)

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=Payment)
def create_subscription(sender, instance, *args, **kwargs):
    if instance:
        Subscription.objects.create(subscriber=instance, expires_in=dt.now(
        ).date() + timedelta(days=instance.duration))


# User Subscription
class Subscription(models.Model):
    subscriber = models.ForeignKey(
        Payment, related_name='subscription', on_delete=models.CASCADE, default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subscriber.user.username


@ receiver(post_save, sender=Subscription)
def update_active(sender, instance, *args, **kwargs):
    if instance.expires_in == today:
        subscription = Subscription.objects.get(id=instance.id)
        subscription.delete()


@ receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}, here is your password reset token: {} Copy and past in your app".format(
        reset_password_token.user.username, reset_password_token.key,)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        fail_silently=False
    )
