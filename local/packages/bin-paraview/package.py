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
            if '+client' in self.spec:
                _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-MPI-Linux-64bit.tar.gz'
            else:
                _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-osmesa-MPI-Linux-64bit.tar.gz'                
        return _url_str.format(version.up_to(2),version)

    variant('client', default=False, description='Get build with Paraview client')
    
    version('5.6.0', sha256='04bb09a4aa9b539f5973653939a8d8cb16ab27579a6a499abdf071013c964fb5', expand=False)
    version('5.5.2', sha256='b2ba52093bd04331217f32805d810198bccfa582de78d46185e95d0f39857772', expand=False)
    version('5.4.1', sha256='e0848896ee9ca0e2d52efcb4e6435a56bc352e30d23f0cc3fc542b44424c357a', expand=False)

    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', join_path(self.prefix,'bin'))
