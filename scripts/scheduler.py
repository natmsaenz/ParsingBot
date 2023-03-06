from os import path, system
from json import load, dump

from .setup import load_settings


def write_task():
    script_path = path.dirname(__file__)
    settings_path = path.join(script_path, "../settings.txt")

    if path.exists(settings_path):
        settings_file = open(settings_path)
        settings = load(settings_file)
        settings.close()

        settings["HAS_BEEN_SCHEDULED"] = True

        settings_file = open(settings_path, "w")
        dump(settings, settings_file)
        settings_file.close()


def setup_schedule():
    *_, HAS_BEEN_SCHEDULED, SCHEDULE_TIME, SCHEDULE_DAY = load_settings()

    if (SCHEDULE_DAY != None and SCHEDULE_TIME != None):
        parsing_bot_path = path.join(path.dirname(__file__), "ParsingBot.py")
        command = f"py {parsing_bot_path}"

        if (HAS_BEEN_SCHEDULED != False):
            system(
                f'SCHTASKS /CHANGE /TN "AUTOMATED\PARSINGBOT" /ST {SCHEDULE_TIME}')
        else:
            write_task()
            system(
                f'SCHTASKS /CREATE /SC {SCHEDULE_DAY} /TN "AUTOMATED\PARSINGBOT" /TR {command} /ST {SCHEDULE_TIME}')
