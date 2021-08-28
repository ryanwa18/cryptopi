# cryptopi
A repository built to easily display the price of BTC and ETH with a Raspberry Pi and an adafruit eink bonnet.

## Initial Setup

Download Setup Script:

```
wget https://raw.githubusercontent.com/ryanwa18/cryptopi/main/setup.sh
```

Change Permissions:

```
chmod +x setup.sh
```

Run Setup Script:

```
bash setup.sh
```

After Reboot:
```
cd ~/cryptopi
python display_price.py
```
