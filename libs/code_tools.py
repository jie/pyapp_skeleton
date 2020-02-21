import shortuuid
import string
import re

def get_shortuuid(length=10):
    return shortuuid.ShortUUID(string.ascii_uppercase + string.digits).random(
        length=length
    )

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def get_chinese(s):
    s = s.strip()
    pat = re.compile(r"[\u4e00-\u9fa5]+")
    result = pat.findall(s)
    if not result:
        return ""
    return "".join(result).strip()


def get_english(s):
    s = s.strip()
    pat = re.compile(r"[a-zA-Z\s]+")
    result = pat.findall(s)
    if not result:
        return ""
    return "".join(result).strip()