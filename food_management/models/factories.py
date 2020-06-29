import factory, factory.django, factory.fuzzy

from datetime import datetime

from food_management.models import *
from food_management.constants.enums import *


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user %d' % n)


UNITS_CHOICE = [UnitType.get_list_of_tuples()]

CATEGORY_CHOICE = [CategoryType.get_list_of_tuples()]

class ItemsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Items

    item = factory.Iterator(['Idly', 'Dosa', 'Chutney', 'Rice', 'Brinjal', 'Curd', 'Poori', 'PotatoCurry', 'Roti'])
    units = factory.fuzzy.FuzzyChoice(UNITS_CHOICE, getter=lambda c: c[0])
    category = factory.fuzzy.FuzzyChoice(CATEGORY_CHOICE, getter=lambda c: c[0])

MEAL_CHOICE = [TypeOfMeal.get_list_of_tuples()]

class MealFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Meal

    meal_type = factory.fuzzy.FuzzyChoice(MEAL_CHOICE, getter=lambda c: c[0])
    from_time_string = '07:00'
    to_time_string = '10:00'
    date = factory.LazyFunction(datetime.now)

MEAL_COURSE_CHOICE = [CourseType.get_list_of_tuples()]

class MealCourseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = MealCourse

    meal = factory.SubFactory(MealFactory)
    item = factory.SubFactory(ItemsFactory)
    quantity = factory.fuzzy.FuzzyInteger(1,7)
    meal_course = factory.fuzzy.FuzzyChoice(MEAL_COURSE_CHOICE, getter=lambda c: c[0])

class UserMealStatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserMealStatus

    meal_course = factory.SubFactory(MealCourseFactory)
    item = factory.SelfAttribute('meal_course.item')
    meal = factory.SelfAttribute('meal_course.meal')
    custom_meal_quantity = factory.SelfAttribute('meal_course.quantity')
    user = factory.SubFactory(UserFactory)

    class Params:
        status = factory.Trait(
            custom_meal_quantity=factory.fuzzy.FuzzyInteger(1,5)
        )

class UserRatingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserRating

    user = factory.SubFactory(UserFactory)
    meal = factory.SubFactory(MealFactory)
    item = factory.SubFactory(ItemsFactory)
    taste = factory.fuzzy.FuzzyInteger(1,5)
    quality = factory.fuzzy.FuzzyInteger(1,5)

class UserFeedbackFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserFeedback

    description = "Nice"
    meal = factory.SubFactory(MealFactory)
    user = factory.SubFactory(UserFactory)

