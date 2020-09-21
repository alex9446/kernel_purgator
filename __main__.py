import sys

import pyperclip

BASE_CMD = 'sudo apt purge'  # base command to use for kernel purging
KERNEL_MODELS = [  # kernel models by purging order
    'linux-modules-extra-{}-{}-generic',
    'linux-image-{}-{}-generic',
    'linux-modules-{}-{}-generic',
    'linux-headers-{}-{}-generic',
    'linux-headers-{}-{}'
]


def main() -> None:
    if len(sys.argv) < 3:
        print('Usage: python {} <kernel_version> <kernel_abi>[...]'
              .format(sys.argv[0]))
    else:
        kernel_version = sys.argv[1]
        kernel_abi_list = sys.argv[2:]
        print('Kernel version: {}\nKernel ABI: {}\n'
              .format(kernel_version, ', '.join(kernel_abi_list)))
        for kernel_model in KERNEL_MODELS:
            command = BASE_CMD
            for kernel_abi in kernel_abi_list:
                command += ' '
                command += kernel_model.format(kernel_version, kernel_abi)
            pyperclip.copy(command)
            print(command + '  <-- Command copied to clipboard')
            if kernel_model is not KERNEL_MODELS[-1] \
                    and input('Pass to next command? [Y/n] ') == 'n':
                break


if __name__ == '__main__':
    main()
