from pipx.constants import ExitCode


def show_help(parser):
    parser.print_help()
    return ExitCode(1)
