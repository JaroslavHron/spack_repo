from spack import *


class BinSage(Package):
    """ SageMath - Open Source Mathematics Software. (official binary package)"""

    homepage = "http://www.sagemath.org/"
    url      = "http://www.sagemath.org/"

    def url_for_version(self, version):
        url='https://mirror.koddos.net/sagemath/linux/64bit/sage-{0}-Ubuntu_16.04-x86_64.tar.bz2'
        #url='http://files.sagemath.org/linux/64bit/sage-{0}-Ubuntu_16.04-x86_64.tar.bz2'
        return url.format(version)

    version('8.6', sha256='928589e68e1a05ad9937694189ff0775d1c73b2cbe73e53c1551d0e8b08643bb')    
      
    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)
        mkdirp(prefix.bin)
        symlink('../sage', '{0}/sage'.format(self.prefix.bin))
        
#    def setup_environment(self, spack_env, run_env):
#        run_env.prepend_path('PATH', join_path(self.prefix.bin))
