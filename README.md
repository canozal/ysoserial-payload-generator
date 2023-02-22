# ysoserial-payload-generator

A Python script that generates serialized payloads for Java deserialization attacks using the `ysoserial` library.

## Description

This Python script uses the `ysoserial` library to generate serialized payloads for Java deserialization attacks. The script allows users to specify the gadget and command to use for generating the payload, and outputs the URL-encoded payload to a file. The script also includes support for an optional output file name.

## Usage

To use the script, simply run it with the desired gadget and command as arguments, like this:

python3 ysoserial_payload_generator.py -g CommonsCollections1 -c 'rm /home/carlos/morale.txt' -o mypayload.txt

This will generate a payload using the `CommonsCollections1` gadget and the `rm /home/carlos/morale.txt` command, URL-encode it, and output it to a file called `mypayload.txt`. If you omit the `-o` option, the payload will be output to a file called `payload.txt`.

## Dependencies

This script requires the `ysoserial` library to be installed in the same directory as the script. You can download the library from the [ysoserial GitHub repository](https://github.com/frohoff/ysoserial).

## Disclaimer

Please note that using this script to generate payloads for exploitation is only legal when used for authorized penetration testing or other security research purposes. Using the script for malicious purposes is illegal and can result in serious legal consequences.

## License

This script is licensed under the [MIT License](LICENSE).
