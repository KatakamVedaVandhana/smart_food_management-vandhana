from django_swagger_utils.utils.test import CustomAPITestCase

from food_management.models.factories import *

class CustomTestUtils(CustomAPITestCase):

    def get_home_page_factories(self, date):

        meal1 = MealFactory(date=date, meal_type=TypeOfMeal.breakfast.value)
        meal2 = MealFactory(date=date, meal_type=TypeOfMeal.lunch.value)
        meal3 = MealFactory(date=date, meal_type=TypeOfMeal.dinner.value)

        items = ItemsFactory.create_batch(size=3)
        half_meal1 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[0])
        half_meal2 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[1])
        half_meal3 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[2])

        full_meal1 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[0])
        full_meal2 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[1])
        full_meal3 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[2])

        custom_meal1 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[0], quantity=0)
        custom_meal2 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[1], quantity=0)
        custom_meal3 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[2], quantity=0)

        skip_meal1 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[0])
        skip_meal2 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[1])
        skip_meal3 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[2])

        items = ItemsFactory.create_batch(size=3)
        half_meal1 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal2, item=items[0])
        half_meal2 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal2, item=items[1])
        half_meal3 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal2, item=items[2])

        full_meal1 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal2, item=items[0])
        full_meal2 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal2, item=items[1])
        full_meal3 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal2, item=items[2])

        custom_meal1 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal2, item=items[0], quantity=0)
        custom_meal2 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal2, item=items[1], quantity=0)
        custom_meal3 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal2, item=items[2], quantity=0)

        skip_meal1 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal2, item=items[0])
        skip_meal2 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal2, item=items[1])
        skip_meal3 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal2, item=items[2])

        items = ItemsFactory.create_batch(size=3)
        half_meal1 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal3, item=items[0])
        half_meal2 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal3, item=items[1])
        half_meal3 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal3, item=items[2])

        full_meal1 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal3, item=items[0])
        full_meal2 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal3, item=items[1])
        full_meal3 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal3, item=items[2])

        custom_meal1 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal3, item=items[0], quantity=0)
        custom_meal2 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal3, item=items[1], quantity=0)
        custom_meal3 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal3, item=items[2], quantity=0)

        skip_meal1 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal3, item=items[0])
        skip_meal2 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal3, item=items[1])
        skip_meal3 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal3, item=items[2])

    def get_home_page_factories_with_user_meal_status(self, date):

        self.get_home_page_factories(date=date)
        user_meal1 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=1), meal=Meal.objects.get(id=1), item=Items.objects.get(id=1))
        user_meal2 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=2), meal=Meal.objects.get(id=1), item=Items.objects.get(id=2))
        user_meal3 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=3), meal=Meal.objects.get(id=1), item=Items.objects.get(id=3))

        user_meal4 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=22), meal=Meal.objects.get(id=2), item=Items.objects.get(id=1))
        user_meal5 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=23), meal=Meal.objects.get(id=2), item=Items.objects.get(id=2))
        user_meal6 = UserMealStatusFactory(meal_course=MealCourse.objects.get(id=24), meal=Meal.objects.get(id=2), item=Items.objects.get(id=3))

    def user_rating_factory(self, meal_type, date, user):

        meal1 = MealFactory(meal_type=meal_type, date=date)
        items = ItemsFactory.create_batch(size=3)
        half_meal1 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[0])
        half_meal2 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[1])
        half_meal3 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[2])

        full_meal1 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[0])
        full_meal2 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[1])
        full_meal3 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[2])

        custom_meal1 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[0], quantity=0)
        custom_meal2 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[1], quantity=0)
        custom_meal3 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[2], quantity=0)

        skip_meal1 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[0])
        skip_meal2 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[1])
        skip_meal3 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[2])

        user_rating1 = UserRatingFactory(meal=meal1, item=items[0], user=user)
        user_rating2 = UserRatingFactory(meal=meal1, item=items[1], user=user)
        user_rating3 = UserRatingFactory(meal=meal1, item=items[2], user=user)

        user_feedback = UserFeedbackFactory(meal=meal1, user=user)

    def get_meal_data_factory(self, meal_type, date):

        meal1 = MealFactory(meal_type=meal_type, date=date)
        items = ItemsFactory.create_batch(size=3)
        half_meal1 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[0])
        half_meal2 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[1])
        half_meal3 = MealCourseFactory(meal_course=CourseType.half_meal.value, meal=meal1, item=items[2])

        full_meal1 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[0])
        full_meal2 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[1])
        full_meal3 = MealCourseFactory(meal_course=CourseType.full_meal.value, meal=meal1, item=items[2])

        custom_meal1 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[0], quantity=0)
        custom_meal2 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[1], quantity=0)
        custom_meal3 = MealCourseFactory(meal_course=CourseType.custom_meal.value, meal=meal1, item=items[2], quantity=0)

        skip_meal1 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[0])
        skip_meal2 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[1])
        skip_meal3 = MealCourseFactory(meal_course=CourseType.skip_meal.value, meal=meal1, item=items[2])

