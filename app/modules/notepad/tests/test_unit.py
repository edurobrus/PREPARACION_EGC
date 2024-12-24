import pytest
from unittest.mock import patch, MagicMock
from app.modules.notepad.services import NotepadService
from app.modules.notepad.models import Notepad
from app.modules.auth.models import User
from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from flask_login import current_user

@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234')
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


@pytest.fixture
def notepad_service():
    return NotepadService()

def test_get_all_by_user(notepad_service):
    with patch.object(notepad_service.repository, 'get_all_by_user') as mock_get_all:
        mock_notepads = [MagicMock(id=1), MagicMock(id=2)]
        mock_get_all.return_value = mock_notepads

        user_id = 1
        result = notepad_service.get_all_by_user(user_id)

        assert result == mock_notepads
        assert len(result) == 2
        mock_get_all.assert_called_once_with(user_id)

def test_create(notepad_service):
    with patch.object(notepad_service.repository, 'create') as mock_create:
        mock_notepad = MagicMock(id=1)
        mock_create.return_value = mock_notepad

        title = 'Test Notepad'
        body = 'Test Body'
        user_id = 1

        result = notepad_service.create(title=title, body=body, user_id=user_id)

        assert result == mock_notepad
        assert result.id == 1
        mock_create.assert_called_once_with(title=title, body=body, user_id=user_id)

def test_update(notepad_service):
    with patch.object(notepad_service.repository, 'update') as mock_update:
        mock_notepad = MagicMock(id=1)
        mock_update.return_value = mock_notepad

        notepad_id = 1
        title = 'Updated Notepad'
        body = 'Updated Body'

        result = notepad_service.update(notepad_id, title=title, body=body)

        assert result == mock_notepad
        mock_update.assert_called_once_with(notepad_id, title=title, body=body)

def test_delete(notepad_service):
    with patch.object(notepad_service.repository, 'delete') as mock_delete:
        mock_delete.return_value = True

        notepad_id = 1
        result = notepad_service.delete(notepad_id)

        assert result is True
        mock_delete.assert_called_once_with(notepad_id)

def test_get_notepad(test_client):
    """
    Test retrieving a specific notepad via GET request.
    """
    # Log in the test user
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Create a notepad
    response = test_client.post('/notepad/create', data={
        'title': 'Notepad2',
        'body': 'This is the body of notepad2.'
    }, follow_redirects=True)
    assert response.status_code == 200

    # Get the notepad ID from the database
    with test_client.application.app_context():
        from app.modules.notepad.models import Notepad
        notepad = Notepad.query.filter_by(title='Notepad2', user_id=current_user.id).first()
        assert notepad is not None, "Notepad was not found in the database."

    # Access the notepad detail page
    response = test_client.get(f'/notepad/{notepad.id}')
    assert response.status_code == 200, "The notepad detail page could not be accessed."
    assert b'Notepad2' in response.data, "The notepad title is not present on the page."

    logout(test_client)

def test_edit_notepad(test_client):
    """
    Test editing a notepad via POST request.
    """
    # Log in the test user
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Create a notepad
    response = test_client.post('/notepad/create', data={
        'title': 'Notepad3',
        'body': 'This is the body of notepad3.'
    }, follow_redirects=True)
    assert response.status_code == 200

    # Get the notepad ID from the database
    with test_client.application.app_context():
        from app.modules.notepad.models import Notepad
        notepad = Notepad.query.filter_by(title='Notepad3', user_id=current_user.id).first()
        assert notepad is not None, "Notepad was not found in the database."

    # Edit the notepad
    response = test_client.post(f'/notepad/edit/{notepad.id}', data={
        'title': 'Notepad3 Edited',
        'body': 'This is the edited body of notepad3.'
    }, follow_redirects=True)
    assert response.status_code == 200, "The notepad could not be edited."

    # Check that the notepad was updated
    with test_client.application.app_context():
        notepad = Notepad.query.get(notepad.id)
        assert notepad.title == 'Notepad3 Edited', "The notepad title was not updated."
        assert notepad.body == 'This is the edited body of notepad3.', "The notepad body was not updated."

    logout(test_client)

def test_delete_notepad(test_client):
    """
    Test deleting a notepad via POST request.
    """
    # Log in the test user
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Create a notepad
    response = test_client.post('/notepad/create', data={
        'title': 'Notepad4',
        'body': 'This is the body of notepad4.'
    }, follow_redirects=True)
    assert response.status_code == 200

    # Get the notepad ID from the database
    with test_client.application.app_context():
        from app.modules.notepad.models import Notepad
        notepad = Notepad.query.filter_by(title='Notepad4', user_id=current_user.id).first()
        assert notepad is not None, "Notepad was not found in the database."

    # Delete the notepad
    response = test_client.post(f'/notepad/delete/{notepad.id}', follow_redirects=True)
    assert response.status_code == 200, "The notepad could not be deleted."

    # Check that the notepad was deleted
    with test_client.application.app_context():
        notepad = Notepad.query.get(notepad.id)
        assert notepad is None, "The notepad was not deleted."

    logout(test_client)
