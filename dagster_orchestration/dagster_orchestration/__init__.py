
from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules
)
from .assets import resources

# Define a job that will materialize the assets
update_all_assets = define_asset_job("update_all_assets", selection=AssetSelection.all())


# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
update_all_assets_schedule = ScheduleDefinition(
    job=update_all_assets,
    cron_schedule="0 * * * *",  # every hour
)



defs = Definitions(
    assets=load_assets_from_modules([assets]),
    resources=resources,
    jobs=[update_all_assets],
    schedules=[update_all_assets_schedule]
)

