from worlds.LauncherComponents import Component, Type, components, launch, icon_paths


def run_client(*args: str) -> None:
    from .mario_sports_mix_client.main_client import launch_mario_sports_mix_client as launch_msm_client


    launch(launch_msm_client, name="Mario Sports Mix Client", args=args)



icon_paths["SportMixIcon"] = "ap:worlds.mario_sports_mix/icon/SportMixIcon.png"
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










# There are two optional parameters that are worth drawing attention to here: "game_name" and "supports_uri".
# As you might know, on a room page on WebHost, clicking a slot name opens your locally installed Launcher
# and asks you if you want to open a Text Client.
# If you have "game_name" set on your Component, your user also gets the option to open that instead.
# Furthermore, if you have "supports_uri" set to True, your Component will be passed a uri as an arg.
# This uri contains the room url + port, the slot name, and the password.
# You can process this uri arg to automatically connect the user to their slot without having to type anything.

# As you can see above, the APQuest client has both of these parameters set.
# This means a user can click on the slot name of an APQuest slot on WebHost,
# then click "APQuest Client" instead of "Text Client" in the Launcher popup, and after a few seconds,
# they will be connected and playing the game without having to touch their keyboard once.

# Since a Component is just Python code, this doesn't just work with CommonClient-derived clients.
# You could forward this uri arg to your standalone C++/Java/.NET/whatever client as well,
# meaning just about every client can support this "Click on slot name -> Everything happens automatically" action.
# The author would like to see more clients be aware of this feature and try to support it.