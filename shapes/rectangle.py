from shapes.segment_brezenhem import segment_brezenhem


def rectangle(x1, y1, x2, y2):
    """
    Create rectangle where first coord is left lower corner, second coord is right upper corner
    :param x1: x coord of left lower corner
    :param y1: y coord of left lower corner
    :param x2: x coord of right upper corner
    :param y2: y coord of right upper corner
    :return: list of dots, than describes that rectangle
    """
    output = []
    output.extend(segment_brezenhem(x1, y1, x1, y2))
    output.extend(segment_brezenhem(x1, y2, x2, y2))
    output.extend(segment_brezenhem(x2, y2, x2, y1))
    output.extend(segment_brezenhem(x2, y1, x1, y1))
    return output
