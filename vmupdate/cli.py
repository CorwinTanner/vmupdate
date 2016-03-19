import argparse
import sys

from config import config
from host import upate_all_vms


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config', help='use specified config path')

    args = parser.parse_args()

    config.load(args.config)

    upate_all_vms()


if __name__ == '__main__':
    sys.exit(main())
