import threading as th

class utils:
  def clamp(value, minimum, maximum):
    if value < minimum:
      return minimum
    elif value > maximum:
      return maximum
    else:
      return value
  def wrap(value, min_value, max_value):
    range_size = max_value - min_value + 1
    if value < min_value:
        value2 = max_value - (min_value - value) % range_size + 1
    elif value > max_value:
        value2 = min_value + (value - max_value - 1) % range_size
    else:
        value2=value
    return utils.clamp(value2,min_value,max_value)

