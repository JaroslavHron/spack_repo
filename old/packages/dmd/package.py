from spack import *


class Dmd(Package):
    """
    digital mars D compiler
    """
    homepage = 'http://dlang.org'
    url = "https://downloads.dlang.org/releases/2.x/2.071.1/dmd.2.071.1.linux.tar.xz"

    def url_for_version(self, version):
        return "http://downloads.dlang.org/releases/{0}.x/{1}/dmd.{2}.linux.tar.xz".format(version.up_to(1),version,version)

    version('2.071.1','195d9fd197301e7a6b1dd3e1ee6a0a17')
    
    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path,'linux'), join_path(prefix,'linux'))
        install_tree(join_path(self.stage.source_path,'man'), join_path(prefix,'man'))
        install_tree(join_path(self.stage.source_path,'samples'), join_path(prefix,'samples'))
        install_tree(join_path(self.stage.source_path,'html'), join_path(prefix,'html'))
        install_tree(join_path(self.stage.source_path,'src'), join_path(prefix,'src'))
        ln = which('ln')
        with working_dir(prefix):
            ln('-sf', 'linux/bin64', 'bin') 
            ln('-sf', 'linux/lib64', 'lib') 
