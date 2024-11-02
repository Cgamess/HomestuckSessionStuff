def scale(original_value: int, original_scale: int, new_scale: int) -> int:
    scaled_value = int(round(original_value * (new_scale / original_scale)))
    return scaled_value