diamond-solariskstat
====================

Simple set of [diamond](https://github.com/python-diamond) collectors that use Solaris kstats.

* SolarisFSCollector
  * Collects virtual filesystem statistics for any mount in /etc/mnttab that produces metrics.
* SolarisARCCollector
  * Collects all ARC statistics for the system.
* SolarisNFSCollector
  * Collects NFS statistics for the system.
