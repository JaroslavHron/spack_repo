from spack import *

class BinParaview(Package):
    homepage = 'http://www.paraview.org'
    url      = 'http://www.paraview.org'
    
    @when('@5:')
    def url_for_version(self, version):
        _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-Qt4-OpenGL2-MPI-Linux-64bit.tar.gz'
        return _url_str.format(version.up_to(2),version)

    @when('@:4.99')
    def url_for_version(self, version):
        _url_str = 'http://www.paraview.org/files/v{0}/ParaView-{1}-Qt4-Linux-64bit.tar.gz'
        return _url_str.format(version.up_to(2),version)

    version('4.4.0', '7fe3cf6abd9f150246703e3cb7f05065')
    version('5.1.2', 'a5d036b90b880b1369fa918c7f06f012')
    version('5.1.0', 'f6b5086ab8ae66080f1f4e0fd1ad9b86')
                
    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path,'bin'), join_path(prefix,'bin'))
        install_tree(join_path(self.stage.source_path,'lib'), join_path(prefix,'lib'))
        install_tree(join_path(self.stage.source_path,'share'), join_path(prefix,'share'))
        if spec.satisfies('@:4.99'):
            install_tree(join_path(self.stage.source_path,'doc'), join_path(prefix,'doc'))
