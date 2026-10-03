import app.errors as errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError as e:
            return str(e)
        except errors.NotWearingMaskError:
            continue

    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
