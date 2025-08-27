from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("modelcatconnector")
except PackageNotFoundError:
    __version__ = "dev"
