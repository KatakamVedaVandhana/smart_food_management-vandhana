from collections import defaultdict
from datetime import datetime
from datetime import time
from typing import List, Set
from django.db.models import Prefetch, Count
from food_management.models.meal import Meal
from food_management.models.items import Items
from food_management.models.meal_course import MealCourse
from food_management.models.food_wastage import FoodWastage
from food_management.models.user_meal_status import UserMealStatus
from food_management.exceptions.exceptions import UserHasNoMealCourse
from food_management.constants.constants import \
    DEFAULT_DATE_FORMAT, DEFAULT_TIME_FORMAT
from food_management.constants.enums import TypeOfMeal, CourseType
from food_management.dtos.dtos import (
    ItemAndQuantityDto, CustomeMealUpdateDto, UpdateMealScheduleDto
)
from food_management.interactors.storages.dtos import (
    HomePageDto, ItemDto, MealCourseDto, MealDto, SetMealPreferenceDto,
    MealCourseCompleteDetailsDto, MealScheduleDto, HeadCountDto,
    MealCourseCountDto, ItemsCountDto, FoodWastageDto, ItemAndWastageDto
)
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface

class MealStorageImplementation(MealStorageInterface):

    def check_if_date_has_meals(self, date_obj: datetime) -> bool:
        bool_value = Meal.objects.filter(date=date_obj).exists()
        return bool_value


    def get_home_page(self, date_obj: datetime, user_id: int) -> HomePageDto:
        meal_objs = Meal.objects.filter(
            date=date_obj
        ).prefetch_related('item').prefetch_related('usermealstatus_set')
        item_dtos_list, meal_dtos_list, meal_course_dtos_list = [], [], []
        for meal_obj in meal_objs:
            item_dtos_list += self._convert_item_obj_as_dto(meal_obj)
            meal_dtos_list.append(self._convert_meal_obj_as_dto(meal_obj, date_obj))
            meal_course_dtos_list.append(self._convert_meal_course_obj_as_dto(meal_obj, user_id))
        return HomePageDto(
            items=item_dtos_list,
            meal_course=meal_course_dtos_list,
            meal=meal_dtos_list
        )

    def _convert_meal_obj_as_dto(self, meal_obj, date_obj):
        return MealDto(
            meal_id=meal_obj.id,
            meal_type=meal_obj.meal_type,
            date=date_obj,
            from_time_string=meal_obj.from_time_string,
            to_time_string=meal_obj.to_time_string
        )

    def _convert_meal_course_obj_as_dto(self, meal_obj, user_id):
        user_objs = meal_obj.usermealstatus_set.filter(
            meal=meal_obj, user_id=user_id)
        if user_objs:
            meal_course = user_objs[0].meal_course.meal_course
        else:
            meal_course = 'Full-Meal'
        return MealCourseDto(
            meal_course=meal_course,
            meal_id=meal_obj.id,
            meal_type=meal_obj.meal_type
        )

    def _convert_item_obj_as_dto(self, meal_obj):
        item_dtos_list = []
        item_objs = meal_obj.item.all().distinct()
        for item_obj in item_objs:
            item_dtos_list.append(
                ItemDto(
                    item_id=item_obj.id,
                    category=item_obj.category,
                    units=item_obj.units,
                    item=item_obj.item,
                    meal_id=meal_obj.id
                    )
                )
        return item_dtos_list


    def get_meal_preference(
            self, meal_id: int) -> SetMealPreferenceDto:

        meal_obj = Meal.objects.filter(id=meal_id).\
                                prefetch_related('mealcourse_set')[0]
        meal_course_complete_details_dto = []
        mealcourse_objs = meal_obj.mealcourse_set.all()
        for mealcourse_obj in mealcourse_objs:
            meal_course_complete_details_dto.append(self.\
                _convert_meal_course_obj_into_meal_course_complete_details_dto(
                    mealcourse_obj)
                )
        item_dtos = self._convert_item_obj_as_dto(meal_obj)
        return SetMealPreferenceDto(
            meal_course=meal_course_complete_details_dto,
            items=item_dtos
        )

    def get_meal_id(self, meal_type: TypeOfMeal, date_obj: datetime) -> int:
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        return meal_obj.id

    def check_if_its_valid_meal_id(self, meal_id: int) -> bool:
        bool_value = Meal.objects.filter(id=meal_id).exists()
        return bool_value


    def _convert_meal_course_obj_into_meal_course_complete_details_dto(
            self, mealcourse_obj):
        return MealCourseCompleteDetailsDto(
            item_id=mealcourse_obj.item_id,
            meal_course=mealcourse_obj.meal_course,
            quantity=mealcourse_obj.quantity
        )

    def get_user_meal_course_if_user_has_a_meal(
            self, meal_id: int, user_id: int) -> CourseType:

        query_set = UserMealStatus.objects.filter(
            user_id=user_id, meal_id=meal_id
        )
        if query_set:
            meal_course = query_set[0].meal_course.meal_course
        else:
            raise UserHasNoMealCourse
        return meal_course

    def create_user_meal_status(
            self, user_id: int, meal_id: int, meal_course: CourseType):
        mealcourse_objs = MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)
        
        UserMealStatus.objects.bulk_create([
            UserMealStatus(
                user_id=user_id, meal_id=meal_id,
                meal_course=mealcourse_obj,
                custom_meal_quantity=mealcourse_obj.quantity,
                item_id=mealcourse_obj.item_id
        )
        for mealcourse_obj in mealcourse_objs]
        )
        

    def update_user_meal_status(
            self, meal_id: int, meal_course: CourseType,
            user_id: int):
        mealcourse_objs = list(
            MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)
        )
        usermealstatus_objs = UserMealStatus.objects.filter(meal_id=meal_id, user_id=user_id)
        for index in range (len(mealcourse_objs)):
            usermealstatus_obj = usermealstatus_objs[index]
            usermealstatus_obj.meal_course = mealcourse_objs[index]
            usermealstatus_obj.item_id = mealcourse_objs[index].item_id
            usermealstatus_obj.custom_meal_quantity = mealcourse_objs[index].quantity
            usermealstatus_obj.save()

    def udpate_custom_meal_status(
            self, meal_id: int, meal_course: CourseType, user_id: int,
            items_and_quantities: List[ItemAndQuantityDto]):
        item_and_quantity_dict = {}

        meal_course_objs = MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)
        for item_dto in items_and_quantities:
            item_and_quantity_dict[item_dto.item_id] = item_dto.quantity

        usermealstatus_objs = UserMealStatus.objects.filter(meal_id=meal_id, user_id=user_id)
        for index in range(len(meal_course_objs)):
            usermealstatus_obj = usermealstatus_objs[index]
            usermealstatus_obj.meal_id = meal_id
            usermealstatus_obj.meal_course = meal_course_objs[index]
            usermealstatus_obj.custom_meal_quantity = \
                item_and_quantity_dict[meal_course_objs[index].item_id]
            usermealstatus_obj.item_id = meal_course_objs[index].item_id
            usermealstatus_obj.save()

    def create_custom_meal_status(
            self, meal_id: int, meal_course: CourseType, user_id: int,
            items_and_quantities: List[ItemAndQuantityDto]):
        item_and_quantity_dict = {}
        meal_course_objs = MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)
        for item_dto in items_and_quantities:
            item_and_quantity_dict[item_dto.item_id] = item_dto.quantity
        UserMealStatus.objects.bulk_create([
            UserMealStatus(
                user_id=user_id, meal_course=meal_course_obj,
                item_id=meal_course_obj.item_id, 
                meal_id = meal_id,
                custom_meal_quantity=item_and_quantity_dict[meal_course_obj.item_id]
            )
            for meal_course_obj in meal_course_objs]
        )


    def check_if_user_has_a_meal(
            self, meal_id: int, user_id: int):
        query_set = UserMealStatus.objects.filter(user_id=user_id, meal_id=meal_id)
        if query_set:
            return True
        else: 
            return False

    def check_if_it_has_valid_item_ids_for_that_meal(
            self, items_ids: List[int], meal_id: int):
        meal_obj = Meal.objects.get(id=meal_id)
        item_ids_list = list(meal_obj.item.all().values_list('id', flat=True).distinct())
        print(item_ids_list)
        print(items_ids)
        valid_item_ids = sorted(item_ids_list) == sorted(items_ids)
        print(valid_item_ids)
        return valid_item_ids

    def get_meal_schedule(self, date_obj: datetime, meal_type: TypeOfMeal) -> MealScheduleDto:
        meal_objs = Meal.objects.filter(date=date_obj, meal_type=meal_type).prefetch_related('item')
        item_dtos_list = []
        for meal_obj in meal_objs:
            item_dtos_list += self._convert_item_obj_as_dto(meal_obj)
        meal_dto = self._convert_meal_obj_as_dto(meal_obj, date_obj)
        return MealScheduleDto(
            meal=meal_dto,
            items=item_dtos_list
        )

    def check_if_date_has_a_meal(
            self, date_obj: datetime, meal_type: TypeOfMeal) -> bool:
        bool_value = Meal.objects.filter(meal_type=meal_type, date=date_obj).exists()
        return bool_value


    def create_meal_schedule(
            self, update_meal_schedule_dto: UpdateMealScheduleDto,
            from_time_string: time, to_time_string: time):

        meal_type = update_meal_schedule_dto.meal_type
        date_obj = update_meal_schedule_dto.date

        meal_obj = Meal.objects.create(
                meal_type=meal_type, date=date_obj,
                from_time_string=from_time_string,
                to_time_string=to_time_string
            )
        items_and_quantites = self._map_items_and_their_quantities(
            update_meal_schedule_dto.items
        )
        self._create_meal_course_objects(
            items_and_quantites=items_and_quantites,
            meal_id=meal_obj.id
        )

    def get_items_list(self) -> List[ItemDto]:
        item_objs = Items.objects.all()
        item_dtos = []
        for item_obj in item_objs:
            item_dtos.append(self._convert_item_obj_as_item_dto(item_obj))
        return item_dtos

    def _convert_item_obj_as_item_dto(self, item_obj):
        return ItemDto(
            item_id=item_obj.id,
            item=item_obj.item,
            units=item_obj.units,
            category=item_obj.category,
            meal_id=None
        )

    def check_if_item_exits(self, item_ids: Set[int]):
        existing_item_ids = list(Items.objects.all().values_list('id',flat=True))

        valid_item_ids = all(item_id in existing_item_ids for item_id in item_ids)
        if valid_item_ids:
            return True
        else:
            return False

    def _map_items_and_their_quantities(self, item_dtos):
        items_and_quantites = defaultdict(list)
        for item_dto in item_dtos:
            items_and_quantites[item_dto.item_id].append(item_dto)
        return items_and_quantites

    def update_meal_schedule(self, update_meal_schedule_dto: UpdateMealScheduleDto):
        meal_type = update_meal_schedule_dto.meal_type
        date_obj = update_meal_schedule_dto.date
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        MealCourse.objects.filter(meal=meal_obj).delete()
        items_and_quantites = self._map_items_and_their_quantities(
            update_meal_schedule_dto.items
        )
        self._create_meal_course_objects(
            items_and_quantites=items_and_quantites, meal_id=meal_obj.id
        )

    def _create_meal_course_objects(self,items_and_quantites, meal_id):
        meal_course_list = []
        for key,values in items_and_quantites.items():
            meal_course_list += [
                MealCourse(
                    meal_id=meal_id, item_id=key,
                    meal_course=values[0].meal_course,
                    quantity=values[0].quantity
                ),
                MealCourse(
                    meal_id=meal_id, item_id=key,
                    meal_course=values[1].meal_course,
                    quantity=values[1].quantity
                )
            ]
        for key in items_and_quantites.keys():
            meal_course_list += [
                MealCourse(
                    meal_id=meal_id, item_id=key,
                    meal_course='Custom-meal',
                    quantity=0
                ),
                MealCourse(
                    meal_id=meal_id, item_id=key,
                    meal_course='Skip-meal',
                    quantity=0
                )
            ]
        MealCourse.objects.bulk_create(meal_course_list)

    def get_meal_head_count(self, meal_type: TypeOfMeal, date_obj: datetime) -> HeadCountDto:
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        items_count = {}
        user_meal_course_objs = UserMealStatus.objects.filter(
            meal=meal_obj).prefetch_related('item','meal_course')

        meal_course_count_dto = self._get_meal_course_count(user_meal_course_objs)
        item_count_dto = self._get_items_count(user_meal_course_objs)
        head_count_dto = HeadCountDto(
            items_count=item_count_dto,
            meal_course_count=meal_course_count_dto,
            total_meal_head_count=10,
            completed_meal_head_count=10
        )

    def _get_meal_course_count(self, user_meal_course_objs):

        meal_course_count_list = list(
            user_meal_course_objs.values(
                'meal_course__meal_course'
            ).annotate('meal_course')
        )
        meal_course_count_dto = [
            MealCourseCountDto(
                meal_course=meal_course, meal_course_count=count//3) 
                for meal_course, count in meal_course_count_list
            ]
        return meal_course_count_dto

    def _get_items_count(self, user_meal_course_objs):
        items_count={}
        user_meal_course_objs= user_meal_course_objs.exclude(
            meal_course__meal_course='Skip-meal'
        )
        for user_meal_course_obj in user_meal_course_objs:
            items_count[user_meal_course_obj.item] *= \
                user_meal_course_obj.custom_meal_quantity
        item_count_dto = [
            ItemsCountDto(
                item_id=key.id,
                item=key.item,
                items_count=value
            )
            for key,value in items_count.items()
        ]

    def get_food_wastage(self, meal_type: TypeOfMeal, date_obj: datetime) -> FoodWastageDto:
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        food_wasted, food_prepared = 0, 0
        food_wastage_objs = FoodWastage.objects.filter(meal=meal_obj).select_related('item')

        items_and_wastage_dtos = []
        for food_wastage_obj in food_wastage_objs:
            items_and_wastage_dtos.append(
                self._convert_food_wastage_obj_as_dto(food_wastage_obj)
            )
            food_wasted += food_wastage_obj.food_wasted
            food_prepared += food_wastage_obj.food_prepared
        return FoodWastageDto(
            food_wasted=food_wasted,
            food_prepared=food_prepared,
            items_and_wastage=items_and_wastage_dtos
        )

    def _convert_food_wastage_obj_as_dto(self, food_wastage_obj):
        
        return ItemAndWastageDto(
            item_id=food_wastage_obj.item_id,
            item=food_wastage_obj.item.item,
            food_prepared=food_wastage_obj.food_prepared,
            food_wasted=food_wastage_obj.food_wasted,
            base_unit=food_wastage_obj.base_unit
        )














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































