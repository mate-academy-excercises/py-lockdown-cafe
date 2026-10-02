class VaccineError(Exception):
    pass



class NotVaccinatedError(VaccineError):
    pass
class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    mask = 0

    def __init__(self, mask):
        self.mask += mask

    def __str__(self):
        return f"self.mask is {self.mask}"
