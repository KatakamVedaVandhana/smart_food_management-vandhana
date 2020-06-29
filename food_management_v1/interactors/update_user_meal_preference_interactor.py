from datetime import datetime
from food_management.constants.enums import TypeOfMeal, CourseType
from food_management.exceptions.exceptions import UserHasNoMealCourse
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class UpdateUserMealPreferenceInteractor:

    def __init__(
            self, meal_storage: MealStorageInterface,
            presenter: PresenterInterface):
        self.meal_storage = meal_storage
        self.presenter = presenter

    def update_user_meal_preference(
            self, meal_type: TypeOfMeal, user_id: int, date_obj:datetime,
            meal_course: CourseType):

        is_having_a_meal = self._check_if_date_has_a_meal(meal_type=meal_type, date_obj=date_obj)
        meal_id = self.meal_storage.get_meal_id(meal_type=meal_type, date_obj=date_obj)

        try:
            old_meal_course_type = self.meal_storage.\
                get_user_meal_course_if_user_has_a_meal(
                    user_id=user_id, meal_id=meal_id
                )
        except UserHasNoMealCourse:
            self.meal_storage.create_user_meal_status(
                user_id=user_id, meal_id=meal_id, meal_course=meal_course
            )
            return

        is_same_meal_course = old_meal_course_type == meal_course
        is_not_same_meal_course = not is_same_meal_course

        if is_not_same_meal_course :
            self.meal_storage.update_user_meal_status(
                meal_id=meal_id, meal_course=meal_course,
                user_id=user_id
            )
        else:
            return


    def _check_if_date_has_a_meal(self, meal_type, date_obj):
        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        not_having_a_meal = not is_having_a_meal
        if not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()
        return is_having_a_meal

