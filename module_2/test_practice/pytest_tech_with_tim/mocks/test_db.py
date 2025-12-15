from db import save_user

def test_save_user(mocker):
    mock_conn = mocker.patch('sqlite3.connect')
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Alice", 30)

    mock_conn.assert_called_once_with('users.db')
    mock_cursor.execute.assert_any_call('CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)')
    mock_cursor.execute.assert_any_call('INSERT INTO users (name, age) VALUES (?, ?)', ("Alice", 30))
    mock_conn.return_value.commit.assert_called_once()
    mock_conn.return_value.close.assert_called_once()
