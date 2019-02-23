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
    
    version('4.1.5', sha256='449f7e3bf0bf4680221ff1aeb839a24a8f8f47bf1025e32e2ca5e28968376aa1')
    version('3.0.6', sha256='2174106f4f60c9b5b4c479425e172b9b21aa1869d7cdd0f9a8dd0f05ea70e9c2')
    version('2.15.0', sha256='e2122d2c7d6f81e20f6890c7d291a964ab8d1806bcf125337f2bb7d6c5d47480')
      
    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)

    #def setup_environment(self, spack_env, run_env):
    #    run_env.prepend_path('PATH', join_path(self.prefix.bin))
