import argparse
import os

def parse_command_line_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=(
            'Example Google Cloud IoT Core MQTT device connection code.'))
    parser.add_argument(
            '--algorithm',
            default='RS256',
            choices=('RS256', 'ES256'),
            required=False,
            help='Which encryption algorithm to use to generate the JWT.')
    parser.add_argument(
            '--ca_certs',
            default='roots.pem',
            help=('CA root from https://pki.google.com/roots.pem'))
    parser.add_argument(
            '--cloud_region', default='asia-east1', help='GCP cloud region')
    parser.add_argument(
            '--data',
            default='Hello there',
            help='The telemetry data sent on behalf of a device')
    parser.add_argument(
            '--device_id', default='led-light', required=False, help='Cloud IoT Core device id')
    parser.add_argument(
            '--gateway_id', default='my-gateway', required=False, help='Gateway identifier.')
    parser.add_argument(
            '--jwt_expires_minutes',
            default=120,
            type=int,
            help=('Expiration time, in minutes, for JWT tokens.'))
    parser.add_argument(
            '--listen_dur',
            default=60,
            type=int,
            help='Duration (seconds) to listen for configuration messages')
    parser.add_argument(
            '--message_type',
            choices=('event', 'state'),
            default='event',
            help=('Indicates whether the message to be published is a '
                  'telemetry event or a device state message.'))
    parser.add_argument(
            '--mqtt_bridge_hostname',
            default='mqtt.googleapis.com',
            help='MQTT bridge hostname.')
    parser.add_argument(
            '--mqtt_bridge_port',
            choices=(8883, 443),
            default=8883,
            type=int,
            help='MQTT bridge port.')
    parser.add_argument(
            '--num_messages',
            type=int,
            default=100,
            help='Number of messages to publish.')
    parser.add_argument(
            '--private_key_file',
            default='rsa_private.pem',
            required=False,
            help='Path to private key file.')
    parser.add_argument(
            '--project_id',
            default='my-iot-project-2019',
            help='GCP cloud project name')
    parser.add_argument(
            '--registry_id', 
            default='my-iot-registry', 
            required=False, 
            help='Cloud IoT Core registry id')
    parser.add_argument(
            '--service_account_json',
            default=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
            help='Path to service account json file.')

    return parser.parse_args()
