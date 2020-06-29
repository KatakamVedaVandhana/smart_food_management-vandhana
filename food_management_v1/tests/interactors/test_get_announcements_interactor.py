from datetime import datetime
from unittest.mock import create_autospec
from food_management.interactors.get_announcements_interactor import \
    GetAnnouncementsInteractor
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.constants.constants import DEFAULT_DATE_FORMAT

def test_get_announcements_returns_announcements(
        announcement_dtos, announcement_resoponse_dict):

    #Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_announcements.return_value = announcement_dtos
    presenter.get_announcements_response.return_value = \
        announcement_resoponse_dict
    interactor = GetAnnouncementsInteractor(
        storage=storage, presenter=presenter
    )
    date_as_string = '2020-02-12'
    datetime_obj = datetime.strptime(date_as_string, DEFAULT_DATE_FORMAT)
    #Act
    actual_response_list = interactor.get_announcements(date_obj= datetime_obj)
    #Assert
    assert actual_response_list == announcement_resoponse_dict
    storage.get_announcements.assert_called_once_with(date_obj=datetime_obj)
    presenter.get_announcements_response.assert_called_once_with(announcement_dtos)

def test_get_announcements_returns_empty_list_if_there_are_no_announcements(
        ):

    #Arrange
    empty_list = []
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_announcements.return_value = empty_list
    presenter.get_announcements_response.return_value = empty_list
    interactor = GetAnnouncementsInteractor(
        storage=storage, presenter=presenter
    )
    date_as_string = '2020-03-12'
    datetime_obj = datetime.strptime(date_as_string, DEFAULT_DATE_FORMAT)
    #Act
    actual_response_list = interactor.get_announcements(date_obj= datetime_obj)
    #Assert
    assert actual_response_list == empty_list
    storage.get_announcements.assert_called_once_with(date_obj=datetime_obj)
    presenter.get_announcements_response.assert_called_once_with(empty_list)