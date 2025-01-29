from django.shortcuts import render, redirect
from .models import Notification

def notifications_list(request):
    # Fetch notifications for the logged-in user
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    # Mark a notification as read
    notification = Notification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('notifications_list')

