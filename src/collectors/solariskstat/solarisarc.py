import subprocess
import diamond.collector

class SolarisARCCollector(diamond.collector.Collector):

  def get_default_config(self):
      """
      Returns the default collector settings
      """
      config = super(SolarisARCCollector, self).get_default_config()
      config.update({
          'enabled':  'True',
          'path':     'kstats',
      })
      return config

  def collect(self):
    prefix = 'arcstats.'

    metrics = dict()

    stats = subprocess.Popen("kstat -p zfs:*:arcstats", shell=True, stdout=subprocess.PIPE).stdout.readlines()
    for line in stats:
      metric = line.split(':')[-1].split('\t')
      metrics.update({metric[0]:metric[1].strip()})

    metrics.pop('class')

    for m in metrics:
      self.publish(prefix + m, metrics[m])
