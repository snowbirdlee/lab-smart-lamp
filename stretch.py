from dataclasses import dataclass, field
import time

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
    # ChatGPT. if it's under 0, it's automatically 0. over 100: automatically 100.
    def set_brightness(self, brightness: int): 
        self.brightness = max(0, min(brightness, 100))
    def set_color(self, color: str):
        self.color = color
    def status(self):
        if self.is_on:
            print(f"\n{self.name.title()} [ON]: {self.brightness}% brightness, {self.color}")
        else:
            print(f"\n{self.name.title()} [OFF]: {self.brightness}% brightness, {self.color}")
    def toggle(self): # ChatGPT
        self.is_on = not self.is_on
    def outage(self):
        self.is_on = False
  
    


def main():
    lamp1 = SmartLamp("Desk Lamp")
    lamp1.turn_on()
    lamp1.set_brightness(110)
    lamp1.set_color("orange")
    lamp1.status()
    lamp2 = SmartLamp("Night Lamp")
    lamp2.turn_off()
    lamp2.set_brightness(15)
    lamp2.set_color("blue")
    lamp2.status()
    time.sleep(2)
    
    print("\n\n*Switch*")
    lamp1.toggle()
    lamp1.status()
    lamp2.toggle()
    lamp2.status()
    time.sleep(2)
    
    lamp1.outage()
    lamp2.outage()
    
    print("\n\nThere has been a power outage!")
    lamp1.status()
    lamp2.status()


if __name__ == "__main__":
    main()
