
class Log:
  def __init__(self, inputs, outputs, src=tuple()):
    self.inputs = inputs
    self.outputs = outputs
    self.src = src


class Logger:
  def __init__(self, log: Log):
    self.log_start = log
