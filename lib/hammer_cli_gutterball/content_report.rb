module HammerCLIGutterball
  class ContentReportsCommand < Command
    resource :content_reports

    class ContentHostStatus < InfoCommand
      include HammerCLIForemanTasks::Async

      action :system_status
      command_name 'content-host-status'

      output do
        # TODO
      end

      build_options
    end

    class ContentHostTrend < InfoCommand
      include HammerCLIForemanTasks::Async

      action :system_trend
      command_name 'content-host-trend'

      output do
        # TODO
      end

      build_options
    end

    class StatusTrend < InfoCommand
      include HammerCLIForemanTasks::Async

      action :status_trend
      command_name 'status-trend'

      output do
        # TODO
      end

      build_options
    end

    autoload_subcommands
  end
end
