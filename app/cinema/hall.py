from ..people.customer import Customer
from ..people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:

        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: str
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for cust in customers:
            Customer(cust.name, cust.food).watch_movie(movie_name)
        print(f'"{movie_name}" ended.')

        if type(cleaning_staff) is Cleaner:
            Cleaner(cleaning_staff.name).clean_hall(self.number)
        else:
            Cleaner(cleaning_staff).clean_hall(self.number)
