from spack import *

class BinParaviewServer(Package):
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
            _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-osmesa-MPI-Linux-64bit.tar.gz'                
        return _url_str.format(version.up_to(2),version)

    version('5.6.1', sha256='f24b527fb8be7e16c8f5efbc30537b03088eadf3954be4051b51b8a4ccee4a23', expand=False)

    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', join_path(self.prefix,'bin'))
