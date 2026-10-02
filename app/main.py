import app.errors as errors

def go_to_cafe(friends, cafe):

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except errors.VaccineError as e:
        print(e)
    except errors.NotWearingMaskError as e:
        print(e)
    else:
        return f"Friends can go to {cafe.name}"
    """
    mam listę przyjaciół
    muszę zwrócić wiadomość błędu, która zawiera informację o tym ile znajomych nie ma maski
    minimalna ilość danych : liczba przyjaciół bez maski.
    """
