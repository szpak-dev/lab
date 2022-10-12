class DishError(RuntimeError):
    pass


class DishNotFound(DishError):
    pass


class DishBecameUnavailable(DishError):
    pass


class DailyAvailabilityNotCreatedYet(DishError):
    pass


class RevisionIsOutdated(DishError):
    pass
