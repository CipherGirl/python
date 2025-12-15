from main import get_weather

def test_get_weather():
    assert get_weather(35) == "It's a hot day"
    assert get_weather(25) == "It's a warm day"
    assert get_weather(15) == "It's a cool day"
    assert get_weather(5) == "It's a cold day" 