from conans import ConanFile, CMake
import os

class MyTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "txt"

    def imports(self):
          self.copy("*.dll", dst="bin", src="bin")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join(".","bin", "mytest"))
