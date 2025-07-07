from dataclasses import dataclass, field


@dataclass
class SmartLamp():
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default = False, init = False)
    
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_brightness(self, brightness: int):
        self.brightness = brightness
    def set_color(self, color: str):
        self.color = color
    def status(self):
        if self.is_on:
            print(f"{self.name.title()} [ON]: {self.brightness}% brightness, {self.color}")
        else:
            print(f"{self.name.title()} [OFF]: {self.brightness}% brightness, {self.color}")

def main():
    lamp1 = SmartLamp("Desk Lamp")
    lamp1.turn_on()
    lamp1.set_brightness(80)
    lamp1.set_color("orange")
    lamp1.status()
    
    lamp2 = SmartLamp("Night Lamp")
    lamp2.turn_off()
    lamp2.set_brightness(15)
    lamp2.set_color("blue")
    lamp2.status()


if __name__ == "__main__":
    main()
