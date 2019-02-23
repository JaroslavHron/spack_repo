from spack import *


class BinJulia(Package):
    """The Julia Language: A fresh approach to technical computing (official binary package)"""

    homepage = "http://julialang.org"
    url      = "http://julialang.org"
    git      = "https://github.com/JuliaLang/julia.git"

    def url_for_version(self, version):
        url='https://julialang-s3.julialang.org/bin/linux/x64/{1}/julia-{0}-linux-x86_64.tar.gz'
        return url.format(version, version.up_to(2))

    version('1.1.0', sha256='80cfd013e526b5145ec3254920afd89bb459f1db7a2a3f21849125af20c05471')    
    version('1.0.3', sha256='362ba867d2df5d4a64f824e103f19cffc3b61cf9d5a9066c657f1c5b73c87117', preferred=True)
        
      
    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--strip-components=1', '--file', self.stage.archive_file)

    #def setup_environment(self, spack_env, run_env):
    #    run_env.prepend_path('PATH', join_path(self.prefix.bin))
