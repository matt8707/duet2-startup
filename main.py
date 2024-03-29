""" duet2-startup """

import os
import sys
import usb.core
import usb.util

ID_VENDOR = 0x0c60
ID_PRODUCT = 0x0007


def duet_2(bm_request, w_index, payload):
    """
    pyusb ctrl_transfer
    """

    bm_write = 0x40
    assert dev.ctrl_transfer(bm_write, bm_request, 0, w_index, [payload])

    bm_read = 0xc0
    bytes_to_read = 1
    res = dev.ctrl_transfer(bm_read, bm_request, 0, w_index, bytes_to_read)

    output = {
        "uid": bm_request,
        "chl": w_index + 1,
        "cmd": payload,
        "success": payload == res[0]
    }

    print(output)

uid = {
    "soft_limit": 17,
    "phase": 19,
    "phantom_power": 21,
    "input_type": 22,
    "output_level": 51,
    "level_mic": 52,
    "mute": 53,
    "software_return_source": 54,
    "level_inst": 62,
    "dim": 64,
    "group": 68,
    "sum_to_mono": 70,
    "mixer_level": 76,
    "mixer_pan": 77,
    "mixer_solo": 78,
    "mixer_mute": 79,
    "source": 83,
    "speaker_output_type": 182
}

chl = {
    "1": 0,
    "2": 1,
    "speakers": 0,
    "headphones": 1
}

cmd = {
    "off": 0,
    "on": 1,
    "+4 dBu": 0,
    "-10 dBV": 1,
    "Mic": 2,
    "Inst": 3
}

if __name__ == "__main__":

    try:
        dev = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT)

        duet_2(uid["input_type"], chl["1"], cmd["Inst"])
        duet_2(uid["input_type"], chl["2"], cmd["Inst"])

        # initial input/output gain can be set here
        # /Library/Application Support/Apogee/Settings/DuetII<uid>.xml

    except AttributeError:
        print("Apogee Duet 2 not found...")
        input("Press ENTER to list USB devices")
        print(os.system("system_profiler SPUSBDataType"))

    except usb.core.NoBackendError:
        print("No backend available...")
        input("Press ENTER to run \"brew install libusb\"")
        print(os.system("brew install libusb"))
        sys.exit()
