from food_management.dtos.dtos import CustomeMealUpdateDto
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface

class UpdateUserCustomMealPreferenceInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def update_user_custom_meal_preference(
            self, custom_meal_preference_dto: CustomeMealUpdateDto):
        meal_id = custom_meal_preference_dto.meal_id
        self._check_if_its_valid_meal_id(meal_id=meal_id)

        items_and_quantities = custom_meal_preference_dto.items_and_quantities
        self._check_if_it_has_valid_item_ids(items_and_quantities, meal_id)

        self._check_if_it_has_valid_quantities(items_and_quantities)

        user_id = custom_meal_preference_dto.user_id
        meal_course = custom_meal_preference_dto.meal_course

        is_having_a_meal = self._check_if_user_has_a_meal(
                meal_id=meal_id, user_id=user_id
            )

        if is_having_a_meal:
            self.meal_storage.udpate_custom_meal_status(
                user_id=user_id, meal_id=meal_id, meal_course=meal_course,
                items_and_quantities=custom_meal_preference_dto.items_and_quantities
            )
        else:
            self.meal_storage.create_custom_meal_status(
                user_id=user_id, meal_id=meal_id, meal_course=meal_course,
                items_and_quantities=custom_meal_preference_dto.items_and_quantities
            )
    
    def _check_if_its_valid_meal_id(self, meal_id):
        is_valid_meal_id = self.meal_storage.check_if_its_valid_meal_id(meal_id=meal_id)
        not_a_valid_meal_id = not is_valid_meal_id
        if not_a_valid_meal_id:
            self.presenter.raise_exception_for_invalid_meal_id()

    def _check_if_user_has_a_meal(self, meal_id, user_id):
        is_having_a_meal = self.meal_storage.check_if_user_has_a_meal(
            meal_id=meal_id, user_id=user_id
        )
        return is_having_a_meal

    def _check_if_it_has_valid_item_ids(self, items_and_quantities, meal_id):
        items_ids = [item.item_id for item in items_and_quantities]
        valid_item_ids = self.meal_storage.check_if_it_has_valid_item_ids_for_that_meal(
            items_ids=items_ids, meal_id=meal_id
        )
        not_valid_items = not valid_item_ids
        if not_valid_items:
            self.presenter.raise_exception_for_invalid_item_id()

    def _check_if_it_has_valid_quantities(self, items_and_quantities):
        quantities = [quantity.quantity for quantity in items_and_quantities]
        valid_quantites = all(quantity>0 for quantity in quantities)
        not_valid_quantites = not valid_quantites
        if not_valid_quantites:
            self.presenter.raise_exception_for_invalid_quantity()