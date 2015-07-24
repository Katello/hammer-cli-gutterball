# -*- encoding: utf-8 -*-
$LOAD_PATH.unshift(File.expand_path('../lib', __FILE__))

require 'hammer_cli_gutterball/version'

Gem::Specification.new do |spec|
  spec.authors = ['Adam Price']
  spec.email = ['katello@lists.fedorahosted.org']
  spec.license = 'GPL-3'
  spec.description = 'Hammer-CLI-Gutterball is a Hammer module which provides additional' \
                     ' functionality for use with the foreman_gutterball plugin.'
  spec.summary = 'Gutterball commands for Hammer'
  spec.homepage = 'http://github.com/Katello/hammer-cli-gutterball'

  spec.files = Dir['config/**/*', '{lib}/**/*', 'LICENSE', 'README.md']

  spec.name = 'hammer_cli_gutterball'
  spec.require_paths = %w(lib)
  spec.version = HammerCLIGutterball.version

  spec.add_dependency 'hammer_cli_katello', '~> 0.0.6'

  spec.add_development_dependency 'rake'
  spec.add_development_dependency 'rubocop', '0.24.1'
  spec.add_development_dependency 'rubocop-checkstyle_formatter'
end
