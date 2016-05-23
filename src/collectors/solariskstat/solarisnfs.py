import subprocess
import diamond.collector

class SolarisNFSCollector(diamond.collector.Collector):

  def get_default_config(self):
      """
      Returns the default collector settings
      """
      config = super(SolarisNFSCollector, self).get_default_config()
      config.update({
          'enabled':  'True',
          'path':     'kstats',
      })
      return config

  def collect(self):

    self.collectnfs('v3')
    self.collectnfs('v4')
    self.collectnfs('rpc')

  def collectnfs(self, version):

    prefix = 'nfs.' + str(version) + "."
    command = {
      'v3': "kstat -p nfs:*:rfsproccnt_v3",
      'v4': "kstat -p nfs:*:nfs4* -p nfs:*:rfsproccnt_v4",
      'rpc': "kstat -p unix:*:rpc_cots_server -p nfs:0:nfs_server"
    }

    metrics = dict()

    stats = subprocess.Popen(command.get(str(version)), shell=True, stdout=subprocess.PIPE).stdout.readlines()
    for line in stats:
      metric = line.split(':')[-1].split('\t')
      metrics.update({metric[0]:metric[1].strip()})

    metrics.pop('class')

    for m in metrics:
      self.publish(prefix + m, metrics[m])
