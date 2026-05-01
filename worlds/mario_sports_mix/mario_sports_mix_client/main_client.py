import asyncio
import multiprocessing
import Utils

from CommonClient import get_base_parser, handle_url_arg, gui_enabled, server_loop
from .MSMContext import MSMContext, logger


def launch_mario_sports_mix_client(*args):

    Utils.init_logging("Mario Sports Mix Client")

    async def main(main_args):
        multiprocessing.freeze_support()
        logger.info("main")
        main_parser = get_base_parser()
        parser_args = main_parser.parse_args()

        ctx = MSMContext(parser_args.connect, parser_args.password)
        ctx.auth = main_args.name


        logger.info("Connecting to server...")
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        logger.info("Running game...")
        ctx.dolphin_sync_task = asyncio.create_task(ctx.dolphin_sync_task_func(), name="Dolphin Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task


    import colorama
    parser = get_base_parser(description="Mario Sports Mix Archipelago Client.")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()

    asyncio.run(main(launch_args))
    colorama.deinit()


if __name__ == "__main__":
    launch_mario_sports_mix_client()