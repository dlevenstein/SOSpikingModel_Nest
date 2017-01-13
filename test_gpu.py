import threading
from pycuda import driver
import simulation_data_times


class gpuThread(threading.Thread):
    def __init__(self, gpuid):
        threading.Thread.__init__(self)
        self.ctx  = driver.Device(gpuid).make_context()
        self.device = self.ctx.get_device()

    def run(self):
        simulation_data_times.line_values()
        # Profit!

    def join(self):
        self.ctx.detach()
        threading.Thread.join(self)

driver.init()
ngpus = driver.Device.count()
for i in range(ngpus):
    t = gpuThread(i)
    t.start()
    t.join()
