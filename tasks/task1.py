import logging
from abc import ABC, abstractmethod


log_formatter = logging.Formatter(
    "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(log_formatter)

logger = logging.getLogger("factory_logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, origin: str = None):
        self.make = make
        self.model = model
        self.origin = origin

    def __str__(self):
        return (
            f"{self.make} {self.model} {self.origin if self.origin is not None else ''}"
        )

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car():
        pass

    @abstractmethod
    def create_motorcycle():
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(make: str = "Prototype", model: str = "Example") -> Car:
        return Car(make, model, "(US Spec)")

    def create_motorcycle(
        self, make: str = "Prototype", model: str = "Example"
    ) -> Motorcycle:
        return Motorcycle(make, model, "(US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str = "Prototype", model: str = "Example") -> Car:
        return Car(make, model, "(EU Spec)")

    def create_motorcycle(self, make: str = "Prototype", model: str = "Example"):
        return Motorcycle(make, model, "(EU Spec)")


# Використання
vehicle1 = USVehicleFactory.create_car("Toyota", "Corolla")
logger.info(vehicle1)
vehicle1.start_engine()

vehicle2 = USVehicleFactory.create_motorcycle("Harley-Davidson", "Sportster")
logger.info(vehicle2)
vehicle2.start_engine()

vehicle3 = EUVehicleFactory.create_car("Toyota", "Corolla")
logger.info(vehicle3)
vehicle3.start_engine()

vehicle4 = EUVehicleFactory.create_motorcycle("Harley-Davidson", "Sportster")
logger.info(vehicle4)
vehicle4.start_engine()
