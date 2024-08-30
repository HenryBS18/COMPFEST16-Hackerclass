# Flag
COMPFEST16{L0Ve_m3_s0me_USB_f0rens1CS_fd746ec8b3}

# Solution
the message is in HID Data
```bash
tshark -r traffic.pcapng -T fields -e usbhid.data 'usb.data_len == 8' > res.txt
```

then i make script to parse it.