class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate wash price for a single car without washing it"""
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = (car.comfort_class * diff * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        """Wash single car if possible and return the cost"""
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        """Wash cars that need it and return total income"""
        total = 0.0
        for car in cars:
            total += self.wash_single_car(car)
        return round(total, 1)

    def rate_service(self, rate: int) -> None:
        """Add new rating and recalculate average"""
        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

