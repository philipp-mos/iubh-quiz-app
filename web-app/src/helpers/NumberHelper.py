class NumberHelper:

    @staticmethod
    def convert_from_char_to_number(character: str) -> int:
        """
        Converts a given Character to matching numeric Value
        A = 1; B = 2; C = 3;
        """
        return ord(character.lower()) - 96

    @staticmethod
    def convert_from_number_to_char(number: int, to_upper: bool = False) -> str:
        """
        Converts a given Number to matching Character
        to_upper defines, if created Char is upper- or lowercase
        """
        if to_upper:
            return chr(ord('@') + number)

        return chr(ord('`') + number)
