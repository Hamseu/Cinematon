from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "users"


class Cinema(models.Model):
    cinemas_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    class Meta:
        db_table = "cinemas"
        managed = False

class Hall(models.Model):
    hall_id = models.IntegerField(primary_key=True)
    cinema = models.ForeignKey(Cinema,
                               to_field = "cinemas_id",
                               on_delete=models.CASCADE,
                               related_name = "halls",
                               db_column = "cinema_id"
                               )

    seats_number = models.SmallIntegerField()
    rows_number = models.SmallIntegerField()
    seats_for_row = models.SmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(seats_number=models.F("rows_number") * models.F("seats_for_row")),
                name="check_seats_match"
            )
        ]
        db_table = "halls"
        managed = False

class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    imageurl = models.CharField(max_length = 255)
    genre = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    release_year = models.SmallIntegerField()
    length = models.SmallIntegerField()
    class Meta:
        db_table = "films"
        managed = False

class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    film = models.ForeignKey(Film,
                             to_field = "film_id",
                             on_delete=models.CASCADE,
                             related_name = "sessions",
                             db_column = "film_id")
    hall = models.ForeignKey(Hall,
                             to_field = "hall_id",
                             on_delete=models.CASCADE,
                             related_name = "sessions",
                             db_column = "hall_id")

    cost = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(end_time__gt=models.F("start_time")),
                name="check_time_order"
            )
        ]
        db_table = "sessions"
        managed = False

class BookedTicket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session,
                                to_field = "session_id",
                                on_delete=models.CASCADE,
                                related_name = "tickets",
                                db_column = "session_id"
                                )

    seat = models.SmallIntegerField()
    row = models.SmallIntegerField()

    payment = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["session", "row", "seat"],
                name="unique_seat_per_session"
            )
        ]
        db_table = "booked_tickets"
        managed = False