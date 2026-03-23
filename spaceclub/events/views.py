from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
import qrcode
import base64
from io import BytesIO

from .models import Event, EventRegistration
from .forms import EventRegistrationForm, PaymentVerificationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if request.method == 'POST':
        if event.event_status == 'active':
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                
                # Check for existing registration
                existing_reg = EventRegistration.objects.filter(event=event, email=email).first()
                
                if existing_reg:
                    if existing_reg.payment_status == 'paid':
                        messages.warning(request, f'You are already registered for this event.')
                        return redirect('events:detail', pk=pk)
                    else:
                        messages.info(request, f'You have a pending registration. Please complete your payment.')
                        return redirect('events:payment', registration_id=existing_reg.pk)
                
                registration = form.save(commit=False)
                registration.event = event
                registration.payment_status = 'pending'
                registration.save()
                
                messages.info(request, f'Your details are saved! Registration is INCOMPLETE until payment is verified.')
                return redirect('events:payment', registration_id=registration.pk)
        else:
            messages.error(request, 'Registration for this event is closed.')
            form = EventRegistrationForm()
    else:
        form = EventRegistrationForm()

    return render(request, 'events/detail.html', {
        'event': event,
        'form': form
    })

def payment_process(request, registration_id):
    registration = get_object_or_404(EventRegistration, pk=registration_id)
    event = registration.event
    
    if registration.payment_status == 'paid':
        messages.info(request, 'This registration has already been paid for.')
        return redirect('events:detail', pk=event.pk)
        
    amount = event.registration_fee
    # Ensure amount is formatted to 2 decimal places as required by most UPI apps
    formatted_amount = f"{amount:.2f}"
    
    # Generate UPI URI
    upi_uri = f"upi://pay?pa=9133117272@axl&pn=SpaceClub&am={formatted_amount}&cu=INR"
    
    # Generate QR Code image
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(upi_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert image to base64 to embed in template
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    qr_code_mimetype = "data:image/png;base64," + img_str
    
    if request.method == 'POST':
        form = PaymentVerificationForm(request.POST, instance=registration)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.payment_status = 'paid'
            reg.payment_date = timezone.now()
            reg.save()
            messages.success(request, f'Payment successful! You are fully registered for {event.title}.')
            return redirect('events:detail', pk=event.pk)
    else:
        form = PaymentVerificationForm(instance=registration)
        
    return render(request, 'events/payment.html', {
        'registration': registration,
        'event': event,
        'qr_code_url': qr_code_mimetype,
        'form': form,
    })
