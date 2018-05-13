#!/usr/bin/python3
import click
import struct
import socket


COMMAND_01 = 'off'
COMMAND_02 = 'on'

DATA = {
    #                                                  ... ctrl sum
    #                              ... command
    #                              x01 on/off
    #                              xf2 color change
    #                                  ............... value
    COMMAND_01: b'\x55\x1a\x33\x00\x01\x01\x02\x12\xa9\xbf\xaa\xaa',
    COMMAND_02: b'\x55\x1a\x33\x00\x01\x01\x02\x12\xab\xc1\xaa\xaa',
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


@click.group()
def cli():
    pass


@click.command()
@click.option('--addr', default='192.168.178.42', help='light ip address')
@click.option('--port', default=8899, help='light ip port')
@click.argument('red')
@click.argument('green')
@click.argument('blue')
def rgb(red, green, blue, addr, port):
    command = b'\xf2\x01'
    value = (
        struct.pack('B', int(red)) +
        struct.pack('B', int(green)) +
        struct.pack('B', int(blue))
    )
    data = make_command(command, value)
    send(addr, port, data)


@click.command()
@click.option('--addr', default='192.168.178.42', help='light ip address')
@click.option('--port', default=8899, help='light ip port')
@click.argument('command')
def turn(command, addr, port):
    data = DATA.get(command)
    if not data:
        return
    send(addr, port, data)


cli.add_command(turn)
cli.add_command(rgb)


if __name__ == '__main__':
    cli()
