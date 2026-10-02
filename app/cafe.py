from datetime import date
from email import message

import app.errors as errors

class Cafe:
    def __init__(self, name) -> None:
        self.name = name
    def visit_cafe(self, visitor: dict) -> str:

        massage = "All friends should be vaccinated"
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError(massage)

        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise errors.OutdatedVaccineError(massage)

        elif not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError(1)

        else: return f"Welcome to {self.name}"