from worlds.LauncherComponents import Component, Type, components, launch, icon_paths


def run_client(*args: str) -> None:
    from .mario_sports_mix_client.main_client import launch_mario_sports_mix_client as launch_msm_client


    launch(launch_msm_client, name="Mario Sports Mix Client", args=args)


icon_paths["SportMixIcon"] = f"ap:{__name__}/icon/SportMixIcon.png"
components.append(
    Component(
        "Mario Sports Mix Client",
        func=run_client,
        game_name="Mario Sports Mix",
        component_type=Type.CLIENT,
        supports_uri=True,
        icon="SportMixIcon",

    )
)