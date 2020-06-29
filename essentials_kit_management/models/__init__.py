from essentials_kit_management.models.form import Form
from essentials_kit_management.models.item import Item
from essentials_kit_management.models.section import Section
from essentials_kit_management.models.brand import Brand
from essentials_kit_management.models.user import User
from essentials_kit_management.models.user_item_status import UserItemStatus
from essentials_kit_management.models.user_form_status import UserFormStatus


__all__ = [
    "Form",
    "Item",
    "Section",
    "Brand",
    "User",
    "UserItemStatus",
    "UserFormStatus"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
