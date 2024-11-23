from manimlib.imports import *

class TestScene(Scene):
  def construct(self):
    text = TextMobject("I literally h8 u.")
    text.scale(2)

    self.play(Write(text))
    self.wait()

class TestScene2(Scene):
  def construct(self):
    text = TextMobject("I literally $$3 u.")
    text.scale(2)

    self.play(Write(text))
    self.wait()
