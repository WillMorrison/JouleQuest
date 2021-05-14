# Basic 1kW generator

from src import component
from src import output_component_mixins

class Generator(output_component_mixins.OutputConnectorMixin,
                output_component_mixins.OutputterMixin,
                component.Base):

  def __init__(self):
    super().__init__(name="1kW Perpetual motion generator",
                     nameplate_capacity=1000)
