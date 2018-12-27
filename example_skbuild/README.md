
# Example of python module which is separated to multiple C libraries
Uses scikit-build (skbuild)

All librraries are build from sources and are linked together to create python C extension.
Based on [skbuild-hello-cpp example](https://github.com/henryiii/skbuild-hello-cpp).

# Installation

```
sudo apt install cmake

# if you have pip<10 installed you can just use
pip3 install scikit-build

# build only
python3 setup.py build

# install systemwide
sudo python3 setup.py install

# or rather install to ~/.local/lib/...
python3 setup.py install --user

```
