from spack import *


class BinGmsh(Package):
    """Gmsh is a free 3D finite element grid generator with a built-in CAD engine
    and post-processor. Its design goal is to provide a fast, light and
    user-friendly meshing tool with parametric input and advanced visualization
    capabilities. Gmsh is built around four modules: geometry, mesh, solver and
    post-processing. The specification of any input to these modules is done
    either interactively using the graphical user interface or in ASCII text
    files using Gmsh's own scripting language.
    """

    homepage = 'http://gmsh.info'
    url = 'http://gmsh.info'

    def url_for_version(self, version):
        return 'http://gmsh.info/bin/Linux/gmsh-{0}-Linux64.tgz'.format(version)
    
    
    version('2.13.1', '9ddd236b74669af88035addb3b7cb007')
      
    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path,'bin'), join_path(prefix,'bin'))
        install_tree(join_path(self.stage.source_path,'share'), join_path(prefix,'share'))
