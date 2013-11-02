# Convert Fisher & Paykel .FPH files to csv.

Currently only works for `SUM****.FPH`

```
$ ./fphdump.py data/SUM0001.FPH
timestamp;runtime;usage;leak90;lowPressure;highPressure;apneaEvents;hypoapneaEvents;flowlimitiationEvents;pressure1;pressure2;humiditySetting
2013-10-30 22:42:40;86.4;86.4;22;40;90;1;1;6;40;120;4
2013-10-31 01:16:00;97.2;97.2;16;40;50;0;1;2;40;120;4
```

File format description from [sleepyhead wiki](http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon)