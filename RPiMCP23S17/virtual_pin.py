from gpio.decorators import assert_input, assert_output
from gpio.pin import GenericPin


class VirtualPin(GenericPin):
    INPUT = 0
    OUTPUT = 1

    def __init__(self, mcp, pin_id: int):
        super(VirtualPin, self).__init__(pin_id)
        self.mcp = mcp
        self._callback = None

    def setup(self, mode, *args, **kwargs):
        self.mcp.setDirection(self.pin_id, mode, *args, **kwargs)

    @property
    @assert_input
    def value(self) -> bool:
        return self.mcp.digitalRead(self.pin_id)

    @value.setter
    @assert_output
    def value(self, value: bool):
        self.mcp.digitalWrite(value)

    @assert_input
    def on_interrupt(self, event, callback, **kwargs):
        self.mcp.setInterrupt(self.pin_id, event, **kwargs)
        self._callback = callback
