from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Payment


@shared_task
def send_payment_confirmation_email(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        booking = payment.booking
        user_email = booking.user.email  # assuming Booking has a user FK

        send_mail(
            subject="Booking Payment Confirmation",
            message=f"Hello {booking.user.username},\n\nYour payment for booking {booking.id} was successful.\n\nThank you!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )
    except Payment.DoesNotExist:
        pass
