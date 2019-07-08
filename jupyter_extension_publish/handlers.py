from notebook.base.handlers import IPythonHandler

class TestHandler(IPythonHandler):
    def get(self):
        self.write('hello')
        self.flush()
