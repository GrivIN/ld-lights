import struct
import socket

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Light

COMMAND_01 = 'off'
COMMAND_02 = 'on'

DATA = {
    #                              ........ command
    #                               x01 x01 on/off
    #                               xf2 x01 color change
    #                                       ............ value
    #                                                    .... crc
    #                                                         ........ suffix
    COMMAND_01: b'\x55\x1a\x33\x00 \x01\x01 \x02\x12\xa9 \xbf \xaa\xaa',
    COMMAND_02: b'\x55\x1a\x33\x00 \x01\x01 \x02\x12\xab \xc1 \xaa\xaa',
}


def make_command(command, value):
    prefix = b'\x55\x1a\x33\x00'
    suffix = b'\xaa\xaa'
    data = command + value
    crc = struct.pack('B', sum(data) % 256)
    return prefix + data + crc + suffix


def send(addr, port, data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr, port))
    s.send(data)
    s.close()


@receiver(pre_save, sender=Light)
def send_light_change_request(sender, instance, raw, **kwargs):
    if not raw:
        # turn on
        if instance.is_on:
            command = b'\x01\x01'
            value = b'\x02\x12\xab'
            data = make_command(command, value)
            send(instance.address, instance.port, data)

        # set colors
        command = b'\xf2\x01'
        value = (
            struct.pack('B', int(instance.red)) +
            struct.pack('B', int(instance.green)) +
            struct.pack('B', int(instance.blue))
        )
        data = make_command(command, value)
        send(instance.address, instance.port, data)

        # turn off
        if not instance.is_on:
            command = b'\x01\x01'
            value = b'\x02\x12\xa9'
            data = make_command(command, value)
            send(instance.address, instance.port, data)
