import subprocess
import re
import diamond.collector

class SolarisFSCollector(diamond.collector.Collector):

  def get_default_config(self):
      """
      Returns the default collector settings
      """
      config = super(SolarisFSCollector, self).get_default_config()
      config.update({
          'enabled':  'True',
          'path':     'kstats',
      })
      return config

  def collect(self):
    prefix = 'vopstats.'

    devmap = dict()
    final = dict()

    mnttab = [line.strip() for line in open('/etc/mnttab')]
    for line in mnttab:
      values = line.split('\t')
      mount  = values[1].replace('/', '_')
      device = re.match(".*dev=(.*)", values[-2]).group(1)

      devmap[device] = dict({'mountpoint':mount, 'metrics':dict()})

    for d in devmap:
      stats = subprocess.Popen("kstat -p unix:*:vopstats_" + d, shell=True, stdout=subprocess.PIPE).stdout.readlines()
      for line in stats:
        metric = line.split(':')[-1].split('\t')
        devmap[d]['metrics'].update({metric[0]:metric[1].strip()})

    for d in devmap:
      if len(devmap[d]['metrics']) != 0:
        final[d] = devmap[d]
        final[d]['metrics'].pop('class')

    for f in final:
      for m in final[f]['metrics']:
        self.publish(prefix + final[f]['mountpoint'] + "." + m, final[f]['metrics'][m])
