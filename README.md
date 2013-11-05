# Convert Fisher & Paykel .FPH files to csv.

Currently only works for `SUM****.FPH`


## Dump CPAP sessions
```
$ ./fphdump.py data/SUM0001.FPH
timestamp;runtime;usage;leak90;lowPressure;highPressure;apneaEvents;hypoapneaEvents;flowlimitiationEvents;pressure1;pressure2;humiditySetting
2013-10-30 22:42:40;86.4;86.4;22;40;90;1;1;6;40;120;4
2013-10-31 01:16:00;97.2;97.2;16;40;50;0;1;2;40;120;4
```

# Dump sleep sessions
```
$ ./sleeps.py data/2013-11-05/03330589/SUM0001.FPH
timestamp;runtime;apneaEvents;hypoapneaEvents;flowlimitiationEvents
2013-10-31 20:11:24;28080;3;8;10
2013-11-01 23:06:38;33120;12;17;10
2013-11-02 22:35:00;28080;20;17;14
2013-11-03 22:35:08;1800;0;2;7
2013-11-04 23:05:12;3600;0;0;2
2013-11-05 06:21:02;25920;11;4;8
```

File format description from [sleepyhead wiki](http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon)