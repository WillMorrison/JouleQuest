"""Component defines a base class for things that can participate in a grid."""


class Error(Exception):
  """Base for exceptions raised by this module."""

class ParentClassError(TypeError, Error):
  """Raised for incorrect parent class issues."""

class KindError(Error):
  """Raised for issues with KIND or REQUIRES."""


class _BaseMeta(type):
  """Validates that Components are built sanely."""
  def __init__(cls, name, bases, dct):
    # Have to check that there are parent classes, otherwise this check fails for Base itself
    if bases and not issubclass(bases[-1], Base):
      raise ParentClassError(f'Base must be the rightmost parent class of {bases[-1].__name__}')

    mixins = bases[:-1]
    kinds = set()
    for base in reversed(mixins):
      # Ensure that all parent classes are instances of ComponentMixinBase
      if not issubclass(base, MixinBase):
        raise ParentClassError(f'{base.__name__} is not an instance of ComponentMixinBase')

      # Ensure the KIND attribute is unique among parent classes
      if base.KIND in kinds:
        raise KindError(f'Cannot mix in {base.__name__}, already mixed in something of kind {base.KIND}')

      # Ensure the REQUIRES attribute is satisfied by existing parent classes' KINDs
      for req in base.REQUIRES:
        if req not in kinds:
          raise KindError(f'Cannot mix in {base.__name__}, it requires a parent with KIND {req}')

      kinds.add(base.KIND)


class Base(metaclass=_BaseMeta):
  """Base class for all Components. Ensures the mixins are checked."""
  pass


class MixinBase:
  """Base class for all component mixins. Sets."""

  # KIND must be unique for all mixins used together. Override it in subclasses.
  # Can be used to do runtime checking that conflicting mixins are not used.
  KIND = 'base'

  # Add the KIND of all required other mixin classes here.
  REQUIRES=()

  def __init__(self, *, name):
    self._name = name

  @property
  def name(self):
    return self._name
