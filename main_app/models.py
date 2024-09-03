from django.db import models

from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class EngineType(TimeStampedMixin):
    class Meta:
        verbose_name = _('Engine Type')
        verbose_name_plural = _('Engine Types')

    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return self.name


class AircraftType(TimeStampedMixin):
    class Meta:
        verbose_name = _('Aircraft Type')
        verbose_name_plural = _('Aircraft Types')

    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return self.name


class Category(TimeStampedMixin):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return self.name


class Location(TimeStampedMixin):
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    city = models.CharField(_('city'), max_length=100)


class Requirement(TimeStampedMixin):
    class Meta:
        verbose_name = _('Requirement')
        verbose_name_plural = _('Requirements')

    class TypeChoices(models.TextChoices):
        INITIAL = 'INIT', _('initial')
        EXPERIENCE = 'EXP', _('experience')

    class ValidityChoices(models.IntegerChoices):
        MONTH_6 = 6
        MONTH_12 = 12
        MONTH_24 = 24

    professional_requirement = models.CharField(_('professional_requirement'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    type = models.CharField(_('type'), max_length=50, choices=TypeChoices, default=TypeChoices.INITIAL)
    validity = models.PositiveSmallIntegerField(_('validity'), default=0, choices=ValidityChoices, blank=True)
    duration = models.IntegerField(_('duration'))
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.CASCADE)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    remarks = models.TextField(_('remarks'), blank=True)


class PositionChoices(models.TextChoices):
    class Meta:
        verbose_name = _('Aircraft Type')
        verbose_name_plural = _('Aircraft Types')

    ENG = 'ENG', _('England')


class Skill(TimeStampedMixin):
    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    skill_name = models.CharField(_('skill_name'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.CASCADE)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, max_length=100, on_delete=models.CASCADE)
    position = models.CharField(_('position'), max_length=100, choices=PositionChoices, default=PositionChoices.ENG)
    remarks = models.TextField(_('remarks'), blank=True)


class Staff(TimeStampedMixin):
    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')

    name = models.CharField(_('name'), max_length=100)
    surname = models.CharField(_('surname'), max_length=100)
    post = models.CharField(_('post'), max_length=100)
    certificate_num = models.CharField(_('certificate_num'), max_length=100)
    certificate_date = models.DateField(_('certificate_date'))
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    location = models.CharField(_('location'), max_length=100)
    position = models.CharField(_('position'), max_length=100, choices=PositionChoices, default=PositionChoices.ENG)
    email = models.EmailField(_('email address'), blank=True, null=True)
    phone = models.CharField(_('phone number'), max_length=100, blank=True, null=True)
    remarks = models.TextField(_('remarks'), blank=True)


class ListOfApprovedStaff(TimeStampedMixin):
    class Meta:
        verbose_name = _('List Of Approved Staff')
        verbose_name_plural = _('Lists Of Approved Staff')

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    auth_date = models.DateField(_('auth_date'))
    auth_date_end = models.DateField(_('auth_date_end'))
    # todo Вид выполняемой работы в организации по ТО ??
