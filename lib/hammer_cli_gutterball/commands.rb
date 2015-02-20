module HammerCLIGutterball
  class Command < ::HammerCLIKatello::Command; end

  class InfoCommand < ::HammerCLIKatello::InfoCommand
    def adapter
      :csv
    end
  end
end
