import threading
from pycuda import driver
import nest
import neuron_functions

class gpuThread(threading.Thread):
    def __init__(self, gpuid):
        threading.Thread.__init__(self)
        self.ctx  = driver.Device(gpuid).make_context()
        self.device = self.ctx.get_device()

    def run(self):
        print "%s has device %s, api version %s"  \
             % (self.getName(), self.device.name(), self.ctx.get_api_version())
        # Profit!

    def join(self):
        self.ctx.detach()
        threading.Thread.join(self)

driver.init()
ngpus = driver.Device.count()
for i in range(ngpus):
    t = gpuThread(neuron_functions.neuron_population)
    t.start()
    t.join()
