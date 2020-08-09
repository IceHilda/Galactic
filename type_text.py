def type_text(key_pressed):
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890./ "
    valid_chars += valid_chars.upper()
    if key_pressed in valid_chars:
        return key_pressed


    else:
        return ""
