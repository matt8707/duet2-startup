# duet2-startup

[Apogee Duet 2](https://apogeedigital.com/) reverts to default settings on each boot with M1 macOS Monterey, maybe earlier versions too. This is intended as a startup script to automate setting initial ~~volume level out and~~ input channels to "Instrument", communicating over USB.

```py
duet_2(uid["input_type"], chl["1"], cmd["Inst"])
duet_2(uid["input_type"], chl["2"], cmd["Inst"])
```

```py
# initial output gain can be set here instead
# /Library/Application Support/Apogee/Settings/DuetII8300000000002C71.xml

# duet_2(uid["output_level"], chl["1"], vol_out(-55))
# duet_2(uid["output_level"], chl["2"], vol_out(-55))
```

Thanks to https://github.com/stefanocoding/take_control
