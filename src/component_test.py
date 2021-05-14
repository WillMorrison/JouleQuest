import unittest

from src import component


class TestBaseMeta(unittest.TestCase):

  def testNoMixins(self):
    try:
      class Foo(component.Base):
        pass
    except component.ParentClassError as e:
      self.fail(f'Unexpected ParentClassError: {e}')

  def testWrongMRO(self):
    class Foo(component.MixinBase):
      pass

    with self.assertRaises(component.ParentClassError):
      class Bar(component.Base, Foo):
        pass

  def testNotComponentMixin(self):
    class Foo:
      pass

    with self.assertRaises(component.ParentClassError):
      class Bar(Foo, component.Base):
        pass

  def testOneKind(self):
    class Foo(component.MixinBase):
      KIND='Foo'

    try:
      class Bar(Foo, component.Base):
        pass
    except component.KindError as e:
      self.fail(f'Unexpected KindError: {e}')

  def testUniqueKinds(self):
    class Foo(component.MixinBase):
      KIND='Foo'

    class Bar(component.MixinBase):
      KIND='Bar'

    try:
      class Baz( Foo, Bar, component.Base):
        pass
    except component.KindError as e:
      self.fail(f'Unexpected KindError: {e}')

  def testCollidingKinds(self):
    class Foo(component.MixinBase):
      KIND='Foo'

    class Bar(component.MixinBase):
      KIND='Foo'

    with self.assertRaises(component.KindError):
      class Baz(Foo, Bar, component.Base):
        pass

  def testRequirementMet(self):
    class Foo(component.MixinBase):
      KIND='Foo'

    class Bar(component.MixinBase):
      KIND='Bar'
      REQUIRES=(Foo.KIND,)

    try:
      class Baz(Bar, Foo, component.Base):
        pass
    except component.KindError as e:
      self.fail(f'Unexpected KindError: {e}')

  def testRequirementUnmet(self):
    class Foo(component.MixinBase):
      KIND='Foo'
      REQUIRES=('Bar',)

    with self.assertRaises(component.KindError):
      class Baz(Foo, component.Base):
        pass


class TestMixinBase(unittest.TestCase):

  def testName(self):
    class Component(component.MixinBase, component.Base):
      pass
    c = Component(name='foo')
    self.assertEqual(c.name, 'foo')

  def testUnnamedComponentError(self):
    class Component(component.MixinBase, component.Base):
      pass

    with self.assertRaises(TypeError):
      Component()


if __name__ == '__main__':
  unittest.main()
