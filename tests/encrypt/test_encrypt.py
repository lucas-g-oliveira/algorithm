from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "Python is easy!"
    key1 = 2
    key2 = 5
    key3 = -12

    message_invalid = 5
    key_invalid = "invalid_key"

    assert encrypt_message(message, key1) == "!ysae si noht_yP"
    assert encrypt_message(message, key2) == "ohtyP_!ysae si n"
    assert encrypt_message(message, key3) == "!ysae si nohtyP"

    with pytest.raises(TypeError):
        encrypt_message(message, key_invalid)

    with pytest.raises(TypeError):
        encrypt_message(message_invalid, key1)
