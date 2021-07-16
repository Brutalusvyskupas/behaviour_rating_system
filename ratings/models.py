from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User

# RATE_CHOICES = [
#     (1, '1 - Poor'),
#     (2, '2 - Fair'),
#     (3, '3 - Average'),
#     (4, '4 - Good'),
#     (5, '5 - Great')
# ]


class Review(models.Model):
    reviewed_user = models.ForeignKey(
        User, related_name='eval_user', on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(
        User, related_name='author', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate_professionalism = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])  # unique = True
    rate_teamwork = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate_communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate_organize = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate_problem_solving = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate_personality = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate_reliability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('reviewed_by', 'date'),)

    def __str__(self):
        return self.reviewed_user.first_name + " " + self.reviewed_user.last_name + " Reviewed by: " + self.reviewed_by.first_name + " " + self.reviewed_by.last_name

    # def __unicode__(self):
    #     return str(self.reviewed_user.first_name)
