#exercise 1
print("Exercise 1: Turnstile Finite-State Machine")
from asyncio import Event
from enum import Enum
class State(Enum):
    Locked = 0
    Unlocked = 1
class event(Enum):
    PUSH = 0
    COIN = 1
class Turnstile:
    def __init__(self)->None:
        self._state=State.Locked
    def reset(self)->None:
        """Reset automaton to initial state."""
        self._state=State.Locked
    def handle_event(self,event:event)->None:
        if self._state==State.Locked:
            if event==event.COIN:
                self._state=State.Unlocked
                print(f"{event.name}: Turnstile unlocked")
            elif event==event.PUSH:
                self._state=State.Locked
                print(f"{event.name}: Turnstile remains locked")
        elif self._state==State.Unlocked:
            if event==event.PUSH:
                self._state=State.Locked
                print(f"{event.name}: Turnstile locked")
            elif event==event.COIN:
                self._state=State.Unlocked
                print(f"{event.name}: Turnstile remains unlocked")
    def is_accepting(self)->bool:
        """Check if current state is accepting"""
        return self._state==State.Unlocked
    def run(self,input_sequence: list[str])->bool:
        self.reset()
        for symbol in input_sequence:
            if symbol == "COIN":
                self.handle_event(event.COIN)
            elif symbol == "PUSH":
                self.handle_event(event.PUSH)
        return self.is_accepting()
dfa = Turnstile()
dfa.run(["PUSH","COIN","COIN","PUSH","PUSH"])
print(f"Final state: {'Unlocked' if dfa.is_accepting() else 'Locked'}")
#exercise 2
print("Exercise 2: Simple Motor Control FSM")
from enum import Enum
class System_State(Enum):
    CLOSED = 0
    OPEN = 1
    ERROR = 2
class Input_Event(Enum):
    button_press = 0
    reset = 1
class MotorControlFSM:
    def __init__(self,motor_ok: bool=True)->None:
        self._system_state=System_State.CLOSED
        self.motor_ok=motor_ok
    def start_motor_open(self)->None:
        print("Action: start_motor_open()")
    def start_motor_close(self)->None:
        print("Action: start_motor_close()")
    def clear_error(self)->None:
        print("Action: clear_error()")
    def handle_event(self,event:Input_Event)->None:
        if self._system_state==System_State.CLOSED:
            if event == Input_Event.button_press:
                if self.motor_ok:
                    self.start_motor_open()
                    self._state = System_State.OPEN
                    print(f"{event.name}: System opened")
                else:
                    self._state = System_State.ERROR
                    print(f"{event.name}: System error due to motor failure")
        elif self._system_state==System_State.OPEN:
            if event == Input_Event.button_press:
                if self.motor_ok:
                    self.start_motor_close()
                    self._state = System_State.CLOSED
                    print(f"{event.name}: System closed")
                else:
                    self._state = System_State.ERROR
                    print(f"{event.name}: System error due to motor failure")
        elif self._system_state==System_State.ERROR:
            if event==Input_Event.reset:
                self.clear_error()
                self._system_state=System_State.CLOSED
                print(f"{event.name}: System closed from error")
fsm = MotorControlFSM(motor_ok=True)
fsm.handle_event(Input_Event.button_press)
fsm.handle_event(Input_Event.reset)
#exercise 4
print("Exercise 4: Microwave Oven FSM")
from enum import Enum,auto
class MicrowaveState(Enum):
    Door_open = auto()
    Door_open_with_item = auto()
    Door_shut_with_item = auto()
    Ready_to_cook = auto()
class MicrowaveFSM:
    def __init__(self)->None:
        self._state=MicrowaveState.Door_open
        self.time=0
        print(f"Initial state: {self._state.name}")
    def zero_time(self):
        self.time==0
    def time_remaining(self):
        return self.time>0
    def handle_event(self,event):
        print(f"\nEvent: {event}")
        if self._state==MicrowaveState.Door_open:
            if event=="place_item":
                print("Item placed")
                self._state=MicrowaveState.Door_open_with_item
        elif self._state==MicrowaveState.Door_open_with_item:
            if event=="item_removed":
                print("Item removed")
                self._state=MicrowaveState.Door_open
            elif event=="close_door":
                print("Door closed")
                self._state=MicrowaveState.Door_shut_with_item
        elif self._state==MicrowaveState.Door_shut_with_item:
            if event=="door_opened":
                print("Door opened")
                self._state=MicrowaveState.Door_open_with_item
            elif event=="time_entered":
                self.time=60
                print("Cooking time entered")
                self._state=MicrowaveState.Ready_to_cook
        elif self._state==MicrowaveState.Ready_to_cook:
            if event=="door_opened":
                print("Door opened-cooking cancelled")
                self._state=MicrowaveState.Door_open_with_item
            elif event=="door_closed" and self.zero_time():
                print("No time set")
                self._state=MicrowaveState.Door_shut_with_item
            elif event=="door_closed" and self.time_remaining():
                print("Ready to cook (Waiting for start)")
        print(f"Current state: {self._state.name}")
microwave = MicrowaveFSM()
microwave.handle_event("item_placed")
microwave.handle_event("door_closed")
microwave.handle_event("time_entered")
microwave.handle_event("door_opened")
microwave.handle_event("door_closed")
#exercise 5
print("Exercise 5: Washing Machine Controller")
from enum import Enum, auto
class State_Enumeration(Enum):
    IDLE=auto()
    DOOR_LOCKED=auto()
    FILLING=auto()
    WASHING=auto()
    DRAINING=auto()
    SPINNING=auto()
    COMPLETE=auto()
    ERROR=auto()
class Washing_machine:
    def __init__(self):
        self.state=State_Enumeration.IDLE
        self.door_locked=False
        self.water_level=0
        self.max_safe_level=100
        self.drum_speed=0
        print(f"Initial state: {self.state.name}")
    def  Required_for_any_water_operation(self):
        return self.door_locked
    def prevent_overflow(self):
        return self.water_level<self.max_safe_level
    def required_before_unlocking_door(self,drum_speed):
        return drum_speed<50
    def event_catalog(self,event):
        print(f"\nEvent: {event}")
        if self.state==State_Enumeration.IDLE:
            if event=="door_closed":
                self.door_locked= True
                print("Door locked")
                self.state=State_Enumeration.DOOR_LOCKED
        elif self.state== State_Enumeration.DOOR_LOCKED:
            if event=="start_button" and self.Required_for_any_water_operation():
                print("Starting water fill")
                self.state=State_Enumeration.FILLING
        elif self.state == State_Enumeration.FILLING:
            if event == "water_level_reached" and self.prevent_overflow():
                print("Water level reached")
                self.state = State_Enumeration.WASHING
            elif not self.prevent_overflow():
                print("Overflow detected!")
                self.state = State_Enumeration.ERROR
        elif self.state == State_Enumeration.WASHING:
            if event == "wash_time_complete":
                print("Wash complete, draining water")
                self.state = State_Enumeration.DRAINING
            elif event == "door_opened_during_cycle":
                print("Safety violation!")
                self.state = State_Enumeration.ERROR
        elif self.state == State_Enumeration.DRAINING:
            if event == "drain_complete":
                print("Drain complete, spinning")
                self.state = State_Enumeration.SPINNING
        elif self.state == State_Enumeration.SPINNING:
            if event == "spin_complete":
                print("Spin complete")
                self.state = State_Enumeration.COMPLETE
        elif self.state == State_Enumeration.COMPLETE:
            if event == "door_opened" and self.required_before_unlocking_door(self.drum_speed):
                print("Door unlocked")
                self.door_locked = False
                self.state = State_Enumeration.IDLE
        elif self.state == State_Enumeration.ERROR:
            if event == "reset_button":
                print("System reset")
                self.door_locked = False
                self.water_level = 0
                self.drum_speed = 0
                self.state = State_Enumeration.IDLE
        print(f"Current state: {self.state.name}")
fsm = Washing_machine()
fsm.event_catalog("door_closed")
fsm.event_catalog("start_button")
fsm.water_level = 80
fsm.event_catalog("water_level_reached")
fsm.event_catalog("wash_time_complete")
fsm.event_catalog("drain_complete")
fsm.event_catalog("spin_complete")
fsm.drum_speed = 60
fsm.event_catalog("door_opened")