## What is this

This is an NR-pose demo, which uses 5G CSI results to perform a activities classification, which means with no wearable devices, you can enjoy the somatic game experience in many games like street fighters where limited actions is supported.

## How it stores

- `utils.py` store the udp socket and the instruction indication.

- `keys.py` provides the win32api to simulate user keyboard press event.

- `config.py` binds the activities classification results to the keyboard event.

- `main.py` runs the online classification and perform the somatic game-like input to the SFV.

## What you required
You can do the work by using the follow script:
vk is recommended:
```python

# keyboard (direct keys)
    keys.directKey("a")
    sleep(2)
    keys.directKey("a", keys.key_release)
    sleep(3)
    # keyboard (virtual keys)
    keys.directKey("d", type=keys.virtual_keys)
    sleep(2)
    keys.directKey("d", keys.key_release, keys.virtual_keys)
```
