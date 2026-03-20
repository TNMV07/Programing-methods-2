from enum import Enum 
class State(Enum): 
    SAFE = 0        
    E_OK = 1        
    READY = 2
    MOTOR_ON = 3
class Safetyinterlock:
    def __init__(self)->None:
        self._state=State.SAFE
    def reset(self)->None:
        """Reset automaton to initial state."""
        self._state=State.SAFE
    def transition(self,symbol:str)->None:
        if symbol not in {'S','E','D'}:
            raise ValueError ("Alphabet must be {'S','E','D'}")
        if self._state==State.SAFE:
            if symbol=="D" or symbol=="S":
                self._state=State.SAFE
            elif symbol=="E":
                self._state=State.E_OK
        elif self._state==State.E_OK:
            if symbol=="S" or symbol=="E":
                self._state=State.SAFE
            elif symbol=="D":
                self._state=State.READY
        elif self._state==State.READY:
            if symbol=="D" or symbol=="E":
                self._state=State.SAFE
            elif symbol=="S":
                self._state=State.MOTOR_ON
        elif self._state==State.MOTOR_ON:
            if symbol=="D":
                self._state=State.SAFE
            if symbol=="E":
                self._state=State.READY
            elif symbol=="S":
                self._state=State.MOTOR_ON
    def is_accepting(self)->bool:
        """Check if current state is accepting"""
        return self._state==State.MOTOR_ON
    def run(self,input_sequence: list[str])->bool:
        """Process a sequence of symbols and return True if a valid press cycle is detected at the end"""
        self.reset()
        for symbol in input_sequence:
            self.transition(symbol)
        return self.is_accepting()
dfa = Safetyinterlock()
test_sequences=[
    ["D","E","S"],
    ["S","D"],
    ["E","D","S"],
    ["S","E","E"],
    ["S","E","E","S"],
]
for seq in test_sequences:
    result=dfa.run(seq)
    print(f"{seq} : {'Door opened' if result else 'Door closed'}")
