# need dat katello yo
require 'hammer_cli_katello'

# base commands
require 'hammer_cli_gutterball/commands'

# commands
HammerCLI::MainCommand.lazy_subcommand('content-report',
  _('View Content Reports'),
  'HammerCLIGutterball::ContentReportsCommand',
  'hammer_cli_gutterball/content_report')
