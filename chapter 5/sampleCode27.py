from pixiedust.display.app import *
import matplotlib.pyplot as plt
@PixieApp
class MyApp():
    @route()
    @captureOutput
    def main_screen(self):
        plt.plot([1,2,3,4])
        plt.show()
