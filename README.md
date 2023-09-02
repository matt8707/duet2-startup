# duet2-startup

[Apogee Duet 2](https://apogeedigital.com/) reverts to default settings on each boot with M1 macOS Monterey, maybe earlier versions too. This is intended as a startup script to automate setting input channels to "Instrument".

```py
duet_2(uid["input_type"], chl["1"], cmd["Inst"])
duet_2(uid["input_type"], chl["2"], cmd["Inst"])

# initial input/output gain can be set here
# /Library/Application Support/Apogee/Settings/DuetII<uid>.xml
```

Thanks to https://github.com/stefanocoding/take_control
