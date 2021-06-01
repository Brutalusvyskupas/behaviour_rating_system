from django.db import models

from users.models import User

RATE_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Average'),
    (4, '4 - Good'),
    (5, '5 - Great')
]


class Review(models.Model):
    reviewed_user = models.ForeignKey(
        User, related_name='eval_user', on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User, related_name='author', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate_professionalism = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_teamwork = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_communication = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_organize = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_problem_solving = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_personality = models.PositiveIntegerField(choices=RATE_CHOICES)
    rate_reliability = models.PositiveIntegerField(choices=RATE_CHOICES)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.reviewed_user.first_name + self.reviewed_user.last_name
