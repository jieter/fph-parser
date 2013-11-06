# Convert Fisher & Paykel .FPH parser

Currently only works for `SUM****.FPH` and `DET****.FPH`

File format description from [sleepyhead wiki](http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon)

### Dump CPAP sessions
```
$ ./dumpcsv.py data/SUM0001.FPH
timestamp;runtime;usage;leak90;lowPressure;highPressure;apneaEvents;hypoapneaEvents;flowlimitiationEvents;pressure1;pressure2;humiditySetting
2013-10-30 22:42:40;86.4;86.4;22;40;90;1;1;6;40;120;4
2013-10-31 01:16:00;97.2;97.2;16;40;50;0;1;2;40;120;4
```

### Details
```
$ ./dumpcsv.py data/2013-11-05/DET0001.FPH
timestamp;pressure;totalLeak;apneaDuration;hypoapneaDuration;flowLimitiationDuration
2013-10-30 22:42:40;400;15;0;0;0
2013-10-30 22:44:40;400;15;0;0;0
2013-10-30 22:46:40;500;18;0;0;4
2013-10-30 22:48:40;600;24;0;0;1
2013-10-30 22:50:40;700;20;0;8;0

[...]

2013-11-05 06:39:02;400;20;0;0;0
```

### Dump sleep sessions

CPAP sessions which start less then 2 hours after the end of the last session are grouped together and the values of these sessions are summarized.
```
$ ./sleeps.py data/SUM0001.FPH
timestamp;runtime;apneaEvents;hypoapneaEvents;flowlimitiationEvents
2013-10-30 22:42:40;28080;3;8;10
2013-10-31 20:11:24;33120;12;17;10
2013-11-01 23:06:38;28080;20;17;14
2013-11-02 22:35:00;25200;11;7;2
2013-11-03 22:35:08;29520;4;13;10
2013-11-04 23:05:12;25920;11;4;8
```

