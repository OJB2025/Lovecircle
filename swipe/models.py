from django.conf import settings
from django.db import models


class Swipe(models.Model):
    SWIPE_LEFT = 'left'
    SWIPE_RIGHT = 'right'
    SWIPE_CHOICES = [
        (SWIPE_LEFT, 'Left'),
        (SWIPE_RIGHT, 'Right'),
    ]

    swiper = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='swipes_sent'
    )
    swipee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='swipes_received'
    )
    direction = models.CharField(max_length=10, choices=SWIPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('swiper', 'swipee')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.swiper} -> {self.swipee}: {self.direction}'
