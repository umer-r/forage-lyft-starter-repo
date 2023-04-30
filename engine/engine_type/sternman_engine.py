from engine.engine import Engine

class StrenmanEngine(Engine):
    def __init__(self, check_light_is_on):
        self.check_light_is_on = check_light_is_on

    def needs_service(self):
        if self.check_light_is_on:
            return True
        else:
            return False