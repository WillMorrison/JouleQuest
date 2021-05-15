import unittest

from src import component
from src import output_component_mixins


class TestOutputter(unittest.TestCase):

  def setUp(self):
    class Generator(output_component_mixins.Outputter, component.Base):
      def __init__(self, **kwargs):
          super().__init__(name="test generator", **kwargs)

    self.Generator = Generator

  def testOutputIsNameplateCapacity(self):
    gen = self.Generator(nameplate_capacity=1000)
    self.assertEqual(gen.current_output, 1000)


class TestOutputConnector(unittest.TestCase):

  def setUp(self):
    class Generator(output_component_mixins.OutputConnector,
                    output_component_mixins.Outputter,
                    component.Base):
      def __init__(self, **kwargs):
          super().__init__(name="test generator", **kwargs)

    self.Generator = Generator

  def testOutputIsOnByDefault(self):
    gen = self.Generator(nameplate_capacity=1000)
    self.assertEqual(gen.current_output, 1000)

  def testOutputSwitchedOff(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.toggle_output_connected()
    self.assertEqual(gen.current_output, 0)

  def testOutputSwitchedBackOn(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.toggle_output_connected()
    gen.toggle_output_connected()
    self.assertEqual(gen.current_output, 1000)


class TestOutputConnector(unittest.TestCase):

  def setUp(self):
    class Generator(output_component_mixins.OutputConnector,
                    output_component_mixins.Outputter,
                    component.Base):
      def __init__(self, **kwargs):
          super().__init__(name="test generator", **kwargs)

    self.Generator = Generator

  def testOutputIsOnByDefault(self):
    gen = self.Generator(nameplate_capacity=1000)
    self.assertEqual(gen.current_output, 1000)

  def testOutputSwitchedOff(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.toggle_output_connected()
    self.assertEqual(gen.current_output, 0)

  def testOutputSwitchedBackOn(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.toggle_output_connected()
    gen.toggle_output_connected()
    self.assertEqual(gen.current_output, 1000)


class TestThrottled(unittest.TestCase):

  def setUp(self):
    class Generator(output_component_mixins.ManuallyThrottled,
                    output_component_mixins.Throttled,
                    output_component_mixins.Outputter,
                    component.Base):
      def __init__(self, **kwargs):
          super().__init__(name="test generator", **kwargs)

    self.Generator = Generator

  def testOutputIs100PercentByDefault(self):
    gen = self.Generator(nameplate_capacity=1000)
    self.assertEqual(gen.current_output, 1000)

  def testOutputSetThrottle50Percent(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.set_throttle(0.5)
    self.assertEqual(gen.current_output, 500)

  def testOutputSetOutput(self):
    gen = self.Generator(nameplate_capacity=1000)
    gen.set_output(300)
    self.assertEqual(gen.current_output, 300)

  def testOutputSetThrottleBelowMin(self):
    gen = self.Generator(nameplate_capacity=1000, min_throttle=0)
    gen.set_throttle(-0.5)
    self.assertEqual(gen.current_output, 0)

  def testOutputSetOutputBelowMin(self):
    gen = self.Generator(nameplate_capacity=1000, min_throttle=0)
    gen.set_output(-300)
    self.assertEqual(gen.current_output, 0)

  def testOutputSetThrottleAboveMax(self):
    gen = self.Generator(nameplate_capacity=1000, max_throttle=1.3)
    gen.set_throttle(2)
    self.assertEqual(gen.current_output, 1300)

  def testOutputSetOutputAboveMax(self):
    gen = self.Generator(nameplate_capacity=1000, max_throttle=1.3)
    gen.set_output(2000)
    self.assertEqual(gen.current_output, 1300)

  def testOutputDefaultThrottleWithLowMax(self):
    gen = self.Generator(nameplate_capacity=1000, max_throttle=0.5)
    self.assertEqual(gen.current_output, 500)


if __name__ == '__main__':
  unittest.main()

