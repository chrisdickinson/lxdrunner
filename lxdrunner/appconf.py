import typing
import ipaddress

from goodconf import GoodConf
from pydantic import BaseModel, IPvAnyAddress


class RunnerConf(BaseModel):
    name: str
    labels: frozenset
    image: str
    profiles: list
    runner_os: typing.Literal['linux', 'win', 'osx']
    runner_arch: typing.Literal['x64', 'arm', 'arm64']
    type: typing.Literal['container', 'virtual-machine']

    class Config:
        extra = 'allow'


class AppConfig(GoodConf):
    "Configuration for My App"
    # GitHub
    pat: str
    hooksecret: str
    # LXD
    socket: str
    pkgdir: str
    # Runner
    prefix: str
    setupscript: str
    runnermap: typing.List[RunnerConf]
    activecfg: frozenset
    rundelay: int
    max_workers: int
    # Testing
    def_repo_args: dict = {}
    def_org_args: dict = {}
    # Web
    web_host: IPvAnyAddress = ipaddress.IPv4Address('0.0.0.0')
    web_port: int = 5000
    web_tls: bool = True

    class Config:
        default_files = ["config.yml"]
        file_env_var = "LXDRCFG"


config = AppConfig(load=False)