from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "snake_game"
version = "1.0"

@init
def initialize(project):
    project.build_depends_on("pygame")
