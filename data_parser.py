from psychopy.misc import fromFile
from collections import defaultdict
import re


class DataParser:
    def __init__(self, location):
        self.data = fromFile(location)

    def __str__(self):
        return f"""
        Participant ID:\t {self.data.extraInfo['participant']}
        Session ID:\t {self.data.extraInfo['session']}
        Start Time:\t {self.data.extraInfo['expStart']}
        Frame Rate:\t {self.data.extraInfo['frameRate']}
        """

    def match_entry(self, regular_expression):
        entries = defaultdict(list)
        for entry in self.data.entries:
            for key in entry:
                if re.match(regular_expression, key):
                    entries[key].append(entry)
        return entries

    def __getitem__(self, item):
        if item in [
            "definition",
            "calibration_start",
            "calibration_typing",
            "calibration_end",
            "experiment_start",
            "style_randomizer",
            "window_close",
            "mail_homescreen",
            "mail_notification",
            "mail_content",
            "file_manager_homescreen",
            "file_manager_dragging",
            "file_manager_opening",
            "trash_bin_homescreen",
            "trash_bin_select",
            "trash_bin_confirm",
            "notes_homescreen",
            "notes_repeat",
            "browser_homescreen",
            "browser_navigation",
            "browser_content",
            "experiment_end",
            "pause_on"
        ]:
            return [entry for entry in self.data.entries if f"{item}.started" in entry]
        return [entry for entry in self.data.entries if item in entry]