from datetime import date
import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        message = "All friends should be vaccinated"
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError(message)

        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise errors.OutdatedVaccineError(message)

        elif not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("k")

        else:
            return f"Welcome to {self.name}"
