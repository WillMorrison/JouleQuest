# Basic 1kW generator

class Generator:

  _MAX_OUTPUT = 1000

  def __init__(self):
    self._connected = False
  
  @property
  def name(self):
    return "1kW Perpetual motion generator"

  @property
  def nameplate_capacity(self):
    return self._MAX_OUTPUT

  @property
  def current_output(self):
    return self._MAX_OUTPUT if self._connected else 0

  @property
  def connected(self):
    return self._connected

  def toggle_connection(self):
    self._connected = not self._connected

  def tick(self, environment):
    """Updates internal state every game tick."""
