from src import component


class OutputterMixin(component.MixinBase):
  KIND='outputter'

  def __init__(self, *, nameplate_capacity, **kwargs):
    super().__init__(**kwargs)
    self._nameplate_capacity = nameplate_capacity

  @property
  def nameplate_capacity(self):
    return self._nameplate_capacity

  @property
  def current_output(self):
    return self._nameplate_capacity


class OutputConnectorMixin(component.MixinBase):
  KIND='output_connector'
  REQUIRES=(OutputterMixin.KIND,)

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

