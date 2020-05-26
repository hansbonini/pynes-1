from romLoader import romLoader
from cpu import CPU
from ppu import PPU
import threading
import pygame
import sys

class Console:
    
    def __init__(self):
        romPath = sys.argv[1]

        self.cartridge = romLoader(romPath)

        try:
            self.cartridge.load()
        except:
            print("Couldn't load NES cartridge")

        self.THREAD_MODE = "SINGLE"

        self.CPU = CPU(self)
        self.PPU = PPU(self)


    def powerOn(self):
        self.CPU.run()
    #     self.CPU.start()
    #     self.PPU.start()

if __name__ == '__main__':
    console = Console()
    console.powerOn()