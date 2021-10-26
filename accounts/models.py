from django.db import models
from django.contrib.auth.models import User


class StripeTransaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_transactions")
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, related_name="course_transactions")
    txn_id = models.CharField(max_length=255)
    currency = models.CharField(max_length=10, blank=True, null=True)
    amount = models.IntegerField(default=0)
    stripe_customer = models.CharField(max_length=30, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.txn_id

    def add_student_to_course(self):
        self.course.students.add(self.user)
        self.course.save()
