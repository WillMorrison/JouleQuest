import enum

from src import component

@enum.unique
class Kind(enum.Enum):
  OUTPUTTER = enum.auto()
  OUTPUT_CONNECTOR = enum.auto()
  THROTTLED = enum.auto()
  THROTTLE_CONTROL = enum.auto()


class Outputter(component.MixinBase):
  """Allows components to output power."""
  KIND=Kind.OUTPUTTER

  def __init__(self, *, nameplate_capacity, **kwargs):
    super().__init__(**kwargs)
    self._nameplate_capacity = nameplate_capacity

  @property
  def nameplate_capacity(self):
    return self._nameplate_capacity

  @property
  def current_output(self):
    return self._nameplate_capacity


class OutputConnector(component.MixinBase):
  """Allows the output of components to be switched on and off."""
  KIND=Kind.OUTPUT_CONNECTOR
  REQUIRES=(Kind.OUTPUTTER,)

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self._output_connected = True

  @property
  def current_output(self):
    return super().current_output if self._output_connected else 0

  @property
  def output_connected(self):
    return self._output_connected

  def toggle_output_connected(self):
    self._output_connected = not self._output_connected


class Throttled(component.MixinBase):
  """Allows the output of components to be throttled up or down."""
  KIND=Kind.THROTTLED
  REQUIRES=(Kind.OUTPUTTER,)

  def __init__(self, *, max_throttle=None, min_throttle=0, **kwargs):
    super().__init__(**kwargs)
    self._throttle = 1.0
    self._max_throttle = max_throttle
    self._min_throttle = min_throttle
    self.set_throttle(1.0)

  @property
  def current_output(self):
    return super().current_output * self._throttle

  @property
  def current_throttle(self):
    return self._throttle


class ManuallyThrottled(component.MixinBase):
  """Provides an API for manual throttle control."""
  KIND=Kind.THROTTLE_CONTROL
  REQUIRES=(Kind.THROTTLED,)

  def set_throttle(self, throttle):
    if self._min_throttle is not None:
      throttle = max(self._min_throttle, throttle)
    if self._max_throttle is not None:
      throttle = min(self._max_throttle, throttle)
    self._throttle = throttle

  def set_output(self, output):
    self.set_throttle(output/self.nameplate_capacity)

