class PrimeService:
    @staticmethod
    def is_prime(number: int) -> bool:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            else:
                return True
        else:
            return False
