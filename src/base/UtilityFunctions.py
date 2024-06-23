import hashlib
from PySide6.QtCore import QDateTime


def get_current_time_string():
    current_datetime = QDateTime.currentDateTime()
    current_time_string = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
    return current_time_string

def get_hash_from_time(time_string):
    return hashlib.sha256(time_string.encode()).hexdigest()
