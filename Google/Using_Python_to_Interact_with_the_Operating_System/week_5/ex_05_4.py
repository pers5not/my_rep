import os


def file_read(file_name):
    if not os.path.exists(file_name):
        return ""
    if not os.path.isfile(file_name):
        return ""
    if not os.access(file_name, os.R_OK):
        return ""
