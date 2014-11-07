#!/usr/bin/env python
import configure
from plugins import upCheck

class MonitorBase:
    interval = 300
    plugin = None

class upCheckMonitor(MonitorBase):
    interval = 30
    plugin  = upCheck 
