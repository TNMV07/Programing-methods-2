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