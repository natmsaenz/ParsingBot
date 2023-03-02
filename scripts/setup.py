from json import load
from os import path

DEFAULT_DLT_VIEWER_PATH = "C:\Program Files (x86)\dltviewer\DltViewerSDK\dlt_viewer.exe"
DEFAULT_FOLDERS_TO_CREATE = ["CriticalSoc", "Soc", "Vip", "ISVS", "PATACHMI"]


def load_settings(keyword: str = "ALL"):
    script_path = path.dirname(__file__)
    settings_path = path.join(script_path, "../settings.txt")

    if path.exists(settings_path):
        settings_file = open(settings_path)
        settings = load(settings_file)
        settings_file.close()

        DLT_VIEWER_PATH = settings["DLT_VIEWER_PATH"] if "DLT_VIEWER_PATH" in settings else DEFAULT_DLT_VIEWER_PATH
        FOLDERS_TO_CREATE = settings["FOLDERS_TO_CREATE"] if "FOLDERS_TO_CREATE" in settings and len(settings["FOLDERS_TO_CREATE"])>0 else DEFAULT_FOLDERS_TO_CREATE
        INCIDENCE_KEYWORD = settings["INCIDENCE_KEYWORD"] if "INCIDENCE_KEYWORD" in settings else None
        HAS_BEEN_SCHEDULED = settings["HAS_BEEN_SCHEDULED"] if "HAS_BEEN_SCHEDULED" in settings else False
        SCHEDULE_TIME = settings["SCHEDULE_TIME"] if "SCHEDULE_TIME" in settings else None
        SCHEDULE_DAY = settings["SCHEDULE_DAY"] if "SCHEDULE_DAY" in settings else None

    else:
        DLT_VIEWER_PATH = DEFAULT_DLT_VIEWER_PATH
        FOLDERS_TO_CREATE = DEFAULT_FOLDERS_TO_CREATE
        INCIDENCE_KEYWORD = None
        HAS_BEEN_SCHEDULED = False
        SCHEDULE_TIME = None
        SCHEDULE_DAY = None

    if (keyword == "DLT_VIEWER_PATH"):
        return DLT_VIEWER_PATH
    elif (keyword == "FOLDERS_TO_CREATE"):
        return FOLDERS_TO_CREATE
    elif (keyword == "INCIDENCE_KEYWORD"):
        return INCIDENCE_KEYWORD
    elif (keyword == "HAS_BEEN_SCHEDULED"):
        return HAS_BEEN_SCHEDULED
    elif (keyword == "SCHEDULE_TIME"):
        return SCHEDULE_TIME
    elif (keyword == "SCHEDULE_DAY"):
        return SCHEDULE_TIME

    return DLT_VIEWER_PATH, FOLDERS_TO_CREATE, INCIDENCE_KEYWORD, HAS_BEEN_SCHEDULED, SCHEDULE_TIME, SCHEDULE_DAY