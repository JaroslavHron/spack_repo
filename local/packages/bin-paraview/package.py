from spack import *

class BinParaview(Package):
    homepage = 'http://www.paraview.org'
    url      = 'http://www.paraview.org'

    def url_for_version(self, version):
        if version < Version(5.0) :
            _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-Qt4-Linux-64bit.tar.gz'
        elif version < Version(5.5) :
            _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-Qt5-OpenGL2-MPI-Linux-64bit.tar.gz'
        elif version < Version(5.6) :
            _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-Qt5-MPI-Linux-64bit.tar.gz'
        else :
            _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-MPI-Linux-64bit.tar.gz'
        return _url_str.format(version.up_to(2),version)

    version('5.6.2', sha256='19374dc3fcbc694ef07ef7c44f960fd401141bf01445a13c66af6ac77d5374d3', expand=False)
    version('5.6.1', sha256='5dbf6e2d4f524556ae6f7823ec6581cd163434da36a0caef57a6620f7cd43f9c', expand=False)

    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', join_path(self.prefix,'bin'))
